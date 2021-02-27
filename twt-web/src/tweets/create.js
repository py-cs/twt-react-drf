import React from 'react'

import {apiTweetCreate} from './lookup'


export function TweetCreate(props) {
    const textAreaRef = React.createRef()
    const {didTweet} = (props)

    const handleBackendUpdate = (response, status) => {
        if (status === 201) {
            didTweet(response)
        } else {
            console.log(response)
            alert('Error, please try again')
        }
    }
    
    const handleSubmit = event => {
        event.preventDefault()
        const newTweetContent = textAreaRef.current.value
        apiTweetCreate(newTweetContent, handleBackendUpdate)
        textAreaRef.current.value=''
    }
    
    return (
        <div className={props.className}>
            <div className='col-12 mb-3'>
                <form onSubmit={handleSubmit}>
                    <textarea ref={textAreaRef} className='form-control' required={true}></textarea>
                    <br/>
                    <button type='submit' className='btn btn-primary my-3'>Tweet</button>
                </form>
            </div>
        </div>
    )
}