import {lookup} from '../lookup'


export function apiTweetList(username, callback, nextURL) {
    console.log(`get list with username: ${username}`)
    let endpoint = username ? `/tweets/?username=${username}` : '/tweets/'
    if (nextURL !== null && nextURL !== undefined) {
        endpoint = nextURL.replace('http://localhost:8000/api', '')
    }
    lookup('GET', endpoint, callback)
}

export function apiTweetCreate(newTweet, callback) {
    lookup('POST', '/tweets/create/', callback, {'content': newTweet})
}

export function apiTweetAction(id, action, callback) {
    lookup('POST', '/tweets/action/', callback, {'id': id, 'action': action})
}

export function apiTweetDetail(id, callback) {
    lookup('GET', `/tweets/${id}`, callback)
}