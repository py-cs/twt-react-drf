import React from 'react'

import {apiTweetAction} from './lookup'

export function ActionBtn(props) {
    const {tweet, action, didPerformAction} = props
    const likes = tweet.likes ? tweet.likes : 0
    const className = props.className ? props.className : 'btn btn-primary'
    const actionDisplay = action.display ? action.display : 'Action'
    
    const handleActionBackend = (response, status) => {
        if ((status === 200 || status === 201) && didPerformAction) {
            didPerformAction(response, status)
        }
    }

    const handleClick = (event) => {
        event.preventDefault()
        apiTweetAction(tweet.id, action, handleActionBackend)
    }
    return <button onClick={handleClick} className={className}>{action} {(action === 'Like') ? `(${likes})` : ''}</button>
}