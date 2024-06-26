import axios from "axios";

const baseURL = "http://localhost:8000/"
axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token')

//registration
export function createRegistration(username, email, password) {
    return axios.post("http://localhost:8000/registration/create/", {
        email: email,
        password: password,
    })
}

//wallets
export function createWallet(walletType, seed) {
    return axios.post(`${baseURL}wallets/create/`, {
        wallet_type: walletType,
        seed: seed,
    })
}

export function getWalletsTypes() {
    return axios.get("http://127.0.0.1:8000/wallets/types/")
}

export function getWallets() {
    return axios.get(`${baseURL}wallets/my_wallets/`)
}


//transactions
export function getTransactionList() {
    return axios.get(`${baseURL}transactions/my_transactions/`)
}

export function createTransaction(addressWalletRecipient, walletSender, seed){
    return axios.post(`${baseURL}transactions/create/`, {
        address_wallet_recipient: addressWalletRecipient,
        wallet_sender: walletSender,
        seed: seed
    })
}