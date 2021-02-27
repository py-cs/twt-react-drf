import React from 'react';
import ReactDOM from 'react-dom';
// import './index.css';
import reportWebVitals from './reportWebVitals';
import {TweetsComponent, TweetDetailComponent} from './tweets'
import {ProfileBadgeComponent} from './profiles'

const e = React.createElement
const tweetsElement = document.getElementById('tweets')
if (tweetsElement) {
    ReactDOM.render(e(TweetsComponent, tweetsElement.dataset), tweetsElement)
}

const tweetDetailElements = document.querySelectorAll('.twt-detail')
tweetDetailElements.forEach(container => {
    ReactDOM.render(e(TweetDetailComponent, container.dataset), container)
})

const profileBadgeElements = document.querySelectorAll('.profile-badge')
profileBadgeElements.forEach(container => {
    ReactDOM.render(e(ProfileBadgeComponent, container.dataset), container)
})

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
