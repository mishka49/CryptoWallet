import {Navigate} from "react-router-dom";
import axios from "axios";

export const make_request = (token, setToken, request, url, data = null) => {
    let is_checked_refresh_token = false
    while (true) {
        request(url, data).catch((error) => {

            if (error.response) {
                if (!is_checked_refresh_token) {
                    token.updateToken()
                    setToken(token)
                } else
                    return null;
            }
        }).then((response) => {
            return response.data
        })
    }
}

export const get_request = (url, data = null) => {
    axios.get(url, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer' + token.access
        }
    })
}


export const post_request = (url, data) => {
    axios.post(url, data, {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer' + token.access
        }
    })
}