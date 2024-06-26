import CollapsibleTable from "../components/table";
import DataTable from "../components/dataTable";
import Box from "@mui/material/Box";
import {getWallets, getWalletsTypes} from "../axios.config";
import {useEffect, useState} from "react";
import {Link} from "react-router-dom";
import Button from "@mui/material/Button";

export default function WalletsPage() {
    const [wallets, setWallets] = useState([{id: 0, public_key: '', type: '', total: 0}])

    useEffect(() => {
        getWallets().then((response) => {
            console.log("Wallets", response.data)
            setWallets(response.data)
        })
    }, [])


    const columns = [
        {field: 'id', headerName: 'ID', width: 70},
        {field: 'public_key', headerName: 'Address', width: 130},
        {field: 'type_name', headerName: 'Coin', type: 'number', width: 50,},
        {field: 'total', headerName: 'Current Balance', width: 130},
    ];

    return (
        <Box style={{padding: "2%"}}>
            <Link to="/Wallets/Create">
                <Button variant="contained" href="#contained-buttons">
                    Add
                </Button>
            </Link>
            <DataTable columns={columns} rows={wallets}/>
        </Box>
    )
}