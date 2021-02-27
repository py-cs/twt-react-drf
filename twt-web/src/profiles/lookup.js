import {lookup} from '../lookup'


export function apiProfile(username, callback) {
    lookup('GET', `/profile/${username}`, callback)
}

export function apiProfileFollowToggle(username, action, callback) {
    const data = {action: `${action && action}`.toLowerCase()}
    lookup('POST', `/profile/${username}/follow`, callback, data)
}