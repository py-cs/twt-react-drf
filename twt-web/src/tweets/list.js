import React, {useState, useEffect} from 'react'
import {Tweet} from './detail'

import {apiTweetList} from './lookup'

export function TweetList(props) {
    const {username} = props
    const [tweetsInit, setTweetsInit] = useState([])
    const [tweets, setTweets] = useState([])
    const [nextURL, setNextURL] = useState(null)
    const [loading, setLoading] = useState(false)

    const getNext = (Callback) => apiTweetList(username, Callback, nextURL)

    useEffect(() => {
        apiTweetList(username, (response, status) => {
            if (status === 200) {
                console.log(response)
                setTweetsInit(response.results)
                setNextURL(response.next)
            } else {
                alert(status)
            }
        })

        const handleScroll = () => {
            console.log(window.scrollY + window.innerHeight, document.documentElement.scrollHeight)
            console.log(nextURL, loading)
            if (window.scrollY + window.innerHeight === document.documentElement.scrollHeight) {
                console.log('bottom')
                if (nextURL !== null && !loading) {
                    setLoading(true)
                    const myCallback = (response, status) => {
                        if (status === 200) {
                            setNextURL(response.next)
                            const newTweets = [...tweets].concat(response.results)
                            setTweetsInit(newTweets)
                            setTweets(newTweets)
                            setLoading(false)
                        } else {
                            alert(status)
                        }
                    }
                    console.log(nextURL)
                    getNext(myCallback)
                }
            }
        }
        window.addEventListener('scroll', handleScroll)
        console.log('listener set')
    }, [])

    useEffect(() => {
        const final = ([...props.newTweets].concat(tweetsInit))
        if (final.length !== tweets.length) {
            setTweets(final)
        }
    }, [props.newTweets, tweets, tweetsInit])

    const handleDidRetweet = (newTweet) => {
        const updatedTweetsInit = [...tweetsInit]
        updatedTweetsInit.unshift(newTweet)
        setTweetsInit(updatedTweetsInit)

        const updatedFinalTweets = [...tweets]
        updatedFinalTweets.unshift(tweets)
        setTweets(updatedFinalTweets)
    }

    
    return (
        <React.Fragment>
            <pre>{nextURL}...{loading?1:0}</pre>
            {tweets.map((tweet, index) => {
                // console.log(index, tweet)
                return <Tweet
                    tweet={tweet}
                    didRetweet={handleDidRetweet}
                    className='my-5 py-5 bg-white text-dark'
                    key={`tweet-${index}`} />
            })}
            {/* {nextURL !== null && <button onClick={handleLoadNext} className='btn btn-sm btn-outline-secondary'>Next</button>} */}
        </React.Fragment>
    )
}