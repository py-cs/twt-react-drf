function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export function lookup(method, endpoint, callback, data) {
    let jsonData
    if (data) {
        jsonData = JSON.stringify(data)
    }
    const xhr = new XMLHttpRequest()
    const url = `http://localhost:8000/api${endpoint}`

    xhr.responseType = 'json'
    const token = getCookie('csrftoken')
    xhr.open(method, url)

    xhr.setRequestHeader("Content-Type", "application/json")

    if (token) {
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
        xhr.setRequestHeader("X-CSRFToken", token)
    }

    xhr.onload = () => {
        if (xhr.status === 403) {
            window.location.href = '/login?showLoginRequired=true'
        }
        callback(xhr.response, xhr.status)
    }
    xhr.onerror = e => callback({'message': 'Error occurred'}, 400)
    xhr.send(jsonData)
}
