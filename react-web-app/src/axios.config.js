import axios from "axios";

//registration
export function createRegistration(username, email, password) {
    return axios.post("http://localhost:8000/registration/create/", {
        email: email,
        password: password,
    })
}

//wallets
export function getWallets() {
    axios.get("http://localhost:8000/wallets/my_wallets/", {}).then(
        (response) => {
            console.log("WALLETS", response.data)
        }
    )
}


//transactions
export function getTransactionList() {
    axios.get("http://127.0.0.1:8000/transactions/my_transactions/", {}).then((response) => {
        console.log("TRANSACTION", response.data)
    })
}