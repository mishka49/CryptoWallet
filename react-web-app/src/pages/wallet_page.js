import {createWallet, getWalletsTypes} from "../axios.config";
import {useEffect, useState} from "react";
import SeedGenerator from "../components/seedGenerator"
import Button from "@mui/material/Button";

import {getHash} from '../services/getHash';
import MenuItem from "@mui/material/MenuItem";
import {FormControl, InputLabel, Select} from "@mui/material";


export default function WalletPage() {
    const [walletTypes, setWalletTypes] = useState({0: {id: 0, name: ""}})
    const [seed, setSeed] = useState()
    const [type, setType] = useState()


    useEffect(() => {
        getWalletsTypes().then((response) => {
            setWalletTypes(response.data)
            console.log("TYPES", response.data)
        })
    }, [])

    const getSeed = () => {
        let seedString = ""

        for (const key in seed) {
            seedString += seed[key]
        }

        return getHash(seedString)
    }

    const handleChange = (event) => {
        setType(event.target.value)
    }

    const handleSubmit = (event) => {
        const seed = getSeed()
        createWallet(type, seed).then()
    }


    return (
        <>
            <h1>Create new wallet</h1>
            <FormControl fullWidth>
                <InputLabel id="demo-simple-select-label">Coin type</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={type}
                    label="Wallets type"
                    onChange={handleChange}
                    sx={{margin: "1%"}}
                >
                    <MenuItem value={"BTC"}>Bitcoin</MenuItem>
                    <MenuItem value={"ETH"}>Ethereum</MenuItem>
                </Select>
            </FormControl>

            <div style={{margin: "1%"}}>
                <h3>Create seed phrase</h3>
                <SeedGenerator setSeed={setSeed}/>
            </div>
            <Button variant="contained" href="#contained-buttons" onClick={handleSubmit} sx={{margin: "1%"}}>
                Submit
            </Button>
        </>
    );
}
