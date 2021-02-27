import React, {useState, useEffect} from 'react'
import {apiProfile, apiProfileFollowToggle} from './lookup'
import {UserDisplay, UserPicture} from './components'
import {num} from './utils'

function ProfileBadge(props) {
    const {user, didFollowToggle, profileLoading} = props
    let currentFollowing = profileLoading ? 'Loading...' : user && user.is_following ? 'Unfollow' : 'Follow'
    const handleFollowToggle = (event) => {
        console.log(event)
        event.preventDefault()
        if (didFollowToggle && !profileLoading) {
            didFollowToggle(currentFollowing)
        }
    }
    return user ?
    <div>
        <UserPicture user={user} hideLink />
        <p><UserDisplay user={user} includeFullName hideLink /></p>
        <p>Followers: {num(user.follower_count)}</p>
        <p>Following: {user.following_count}</p>
        <p>{user.location}</p>
        <p>{user.bio}</p>
        <button onClick={handleFollowToggle} className={user.is_following ? 'btn btn-primary' : 'btn btn-primary-outline'}>{currentFollowing}</button>
    </div> : null
}

export function ProfileBadgeComponent(props) {
    const {username} = props
    const [didLookup, setDidLookup] = useState(false)
    const [profile, setProfile] = useState(null)
    const [profileLoading, setProfileLoading] = useState(false)


    const handleBackendLookup = (response, status) => {
        if (status === 200) {
            setProfile(response)
        }
    }
    
    useEffect(() => {
        if (didLookup === false) {
            apiProfile(username, handleBackendLookup)
            setDidLookup(true)
        }
    }, [username, didLookup, setDidLookup])

    const handleNewFollow = (actionVerb) => {
        const myCallback = (responce, status) => {
            console.log(responce, status)
            if (status === 200) {
                setProfile(responce)
            }
            setProfileLoading(false)
        }
        
        setProfileLoading(true)
        apiProfileFollowToggle(username, actionVerb, myCallback)
    }

    return didLookup === false ? "Loading" : profile ? 
    <ProfileBadge user={profile} didFollowToggle={handleNewFollow} profileLoading={profileLoading} /> : null
}
