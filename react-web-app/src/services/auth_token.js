import axios from "axios";


export function getToken(email, password) {
    axios.post("http://127.0.0.1:8000/auth/token/", {
        email: email,
        password: password
    },).then((response) => {
        localStorage.setItem("token", response.data.access)
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token')
    });
}

export function deleteToken() {
    localStorage.removeItem("token")
    delete axios.defaults.headers.common['Authorization']
}

// export function updateToken()
// {
//     axios.post("http://localhost:8000/auth/token/refresh/", {
//         refresh: this.refresh
//     })
//         .then((response) => {
//             localStorage.setItem("token", response.data.access)
//         });
// }