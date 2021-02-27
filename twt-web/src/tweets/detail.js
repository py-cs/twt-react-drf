import React, {useState} from 'react'

import {UserDisplay, UserPicture} from '../profiles'
import {ActionBtn} from './buttons'

export function ParentTweet(props) {
    const {tweet} = props
    return (
        tweet.parent === null ? 
        null :
        <Tweet isRetweet retweeter={props.retweeter} hideActions className={''} tweet={tweet.parent} />
    )
}

export function Tweet(props) {
    // console.log(props)
    const {tweet, isRetweet, retweeter, didRetweet, hideActions} = props
    const [actionTweet, setActionTweet] = useState(props.tweet ? props.tweet : null)
    let className = props.className ? props.className : 'col-10 mx-auto'
    className = isRetweet ? `${className} p-2 border rounded` : className
    const path = window.location.pathname
    const match = path.match(/(?<id>\d+)/)
    const urlTweetId = match ? match.groups.id : -1
    
    const isDetail = `${urlTweetId}` === `${tweet.id}`

    const handlePerformAction = (newActionTweet, status) => {
        if (status === 200) {
            setActionTweet(newActionTweet)
        } else if (status === 201) {
            didRetweet(newActionTweet)
        }
    }

    const handleLink = (event) => {
        event.preventDefault()
        window.location.href = `/${tweet.id}`
    }

    return (
    <div className={className}>
        {isRetweet &&
            <div className='mb-2'>
                <span className='small text-muted'>Retweet via <UserDisplay user={retweeter} /></span>
            </div>
        }
        <div className='d-flex'>
            <div>
                <UserPicture user={tweet.user}/>
            </div>
            <div className='col-11'>
                <div>
                    <p>
                        <UserDisplay includeFullName user={tweet.user}/>
                    </p>
                    <p>{tweet.content}</p>
                    <ParentTweet tweet={tweet} retweeter={tweet.user}/>
                </div>
            </div>
        </div>
        <div className='btn btn-group px-0'>
        {(actionTweet && hideActions !== true) && 
            <React.Fragment>
                <ActionBtn tweet={actionTweet} didPerformAction={handlePerformAction} className='btn btn-primary' action='Like'/>
                <ActionBtn tweet={actionTweet} didPerformAction={handlePerformAction} className='btn btn-outline-primary' action='Unlike'/>
                <ActionBtn tweet={actionTweet} didPerformAction={handlePerformAction} className='btn btn-outline-success' action='Retweet'/>
            </React.Fragment>}
            {isDetail === true ? null : <button onClick={handleLink} className='btn btn-outline-secondary'>View</button>}
        </div>
    </div>
    )
}