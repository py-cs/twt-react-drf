import React from 'react'

export function UserPicture(props) {
    const {user, hideLink} = props
    const userProfileSpan = 
        <span className='mx-1 px-3 py-2 rounded-circle bg-dark text-white'>
            {user.username.toUpperCase()[0]}
        </span>

    return hideLink ? userProfileSpan : <UserLink username={user.username}>{userProfileSpan}</UserLink>
}

export function UserLink(props) {
    const {userName} = props
    const handleUserLink = (event) => {
        window.location.href = `/profile/${userName}`
    }
    return (
        <span className='pointer' onClick={handleUserLink}>
            {props.children}
        </span>
    )
}

export function UserDisplay(props) {
    const {user, includeFullName, hideLink} = props
    const nameDisplay = includeFullName ? `${user.first_name} ${user.last_name} ` : null
    
    return (
        <React.Fragment>
            {nameDisplay}
            {hideLink ? `@${user.username}` : <UserLink userName={user.username}>@{user.username}</UserLink>}
        </React.Fragment>
    )
}
