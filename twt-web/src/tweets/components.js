import React, {useState, useEffect} from 'react'

import {TweetList} from './list'
import {TweetCreate} from './create'
import {Tweet} from './detail'
import {apiTweetDetail} from './lookup'

export function TweetsComponent(props) {
    const [newTweets, setNewTweets] = useState([])

    const handleNewTweet = (newTweet) => {
        let tempNewTweets = [...newTweets]
        tempNewTweets.unshift(newTweet)
        setNewTweets(tempNewTweets)
    }
    
    return (
        <div className={props.className}>
            <TweetCreate didTweet={handleNewTweet} className='col-12 mb-3' />
            <TweetList newTweets={newTweets} {...props}/>
        </div>
    )
}

export function TweetDetailComponent(props) {
    const {id} = props
    const [didLookup, setDidLookup] = useState(false)
    const [tweet, setTweet] = useState(null)

    const handleBackendLookup = (response, status) => {
        if (status === 200) {
            setTweet(response)
        } else {
            alert('Error occured')
        }
    }
    
    useEffect(() => {
        if (!didLookup) {
            apiTweetDetail(id, handleBackendLookup)
            setDidLookup(true)
        }
    }, [id, didLookup, setDidLookup])
    return (
        tweet === null ? null :
        <Tweet tweet={tweet} className={props.className}/>
    )
}