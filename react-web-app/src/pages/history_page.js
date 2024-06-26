import CollapsibleTable from "../components/table";
import Box from "@mui/material/Box";
import {getTransactionList} from "../axios.config";
import {useEffect, useState} from "react";
import DataTable from "../components/dataTable";

export default function HistoryPage() {
    const [transaction, setTransaction] = useState([{id:0,wllet_sender:"", wallet_recipient:"",total:0}])

    useEffect(() => {
        getTransactionList().then((response) => {
            setTransaction(response.data)
        })
    }, [])

    const columns = [
        // {field: 'id', headerName: 'ID', width: 70},
        {field: 'wallet_sender', headerName: 'Sender', width: 130},
        {field: 'wallet_recipient', headerName: 'Recipient', type: 'number', width: 50,},
        {field: 'total', headerName: 'Total', width: 130},
    ];

    return (
        <Box style={{padding: "2%"}}>
            <DataTable columns={columns} rows={transaction}/>
        </Box>
    )
}