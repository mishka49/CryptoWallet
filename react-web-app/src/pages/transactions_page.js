import CollapsibleTable from "../components/table";
import Box from "@mui/material/Box";
import {FormControl, InputLabel, Select} from "@mui/material";
import MenuItem from "@mui/material/MenuItem";
import {useEffect, useState} from "react";
import {createTransaction, getWallets} from "../axios.config";
import {getHash} from "../services/getHash";
import TextField from "@mui/material/TextField";
import SeedGenerator from "../components/seedGenerator";
import Button from "@mui/material/Button";

export default function TransactionsPage() {
    const [wallets, setWallets] = useState([{public_key: ""}])
    const [senderWallet, setSenderWallets] = useState("")

    const [seed, setSeed] = useState()
    const [addressWalletRecipient, setAddressWalletRecipient] = useState()
    const [total, setTotal] = useState()

    useEffect(() => {
        getWallets()
            .then(
                (response) => {
                    setWallets(response.data)
                }
            )
    }, [])

    const getSeed = () => {
        let seedString = ""

        for (const key in seed) {
            seedString += seed[key]
        }

        return getHash(seedString)
    }

    const handleChangeWalletSender = (event) => {
        setSenderWallets(event.target.value)
    }

    const handleChangeWalletRecipient = (event) => {
        setAddressWalletRecipient(event.target.value)
    }

    const handleChangeTotal = (event) => {
        setTotal(event.target.value)
    }

    const handleSubmit = (event) => {
        const seedHash = getSeed()
        createTransaction(addressWalletRecipient, senderWallet, seedHash).then((response) => {
            alert("Transaction was successful")
        })
    }

    return (
        <>
            <FormControl fullWidth sx={{display: "flex", margin: "3%", width: "80%"}}>
                <InputLabel id="demo-simple-select-label">Choose your wallet</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={senderWallet}
                    label="Choose your wallet"
                    onChange={handleChangeWalletSender}
                >
                    {wallets.map((item) => <MenuItem value={item.public_key}>{item.public_key}</MenuItem>)}
                </Select>
                <TextField fullWidth label="Address of recipient (public key)" value={addressWalletRecipient}
                           variant="outlined" width={"100%"}
                           onChange={handleChangeWalletRecipient}/>
                <TextField fullWidth label="total" value={total} variant="outlined" width={"100%"}
                           onChange={handleChangeTotal}/>
            </FormControl>

            <div style={{margine: "2%"}}>
                <h4>Confirm seed phrase</h4>
                <SeedGenerator setSeed={setSeed}/>
                <Button variant="contained" onClick={handleSubmit} sx={{margin: "1%"}}>
                    Submit
                </Button>
            </div>

        </>
    )
}