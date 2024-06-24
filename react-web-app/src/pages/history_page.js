import CollapsibleTable from "../components/table";
import Box from "@mui/material/Box";
import {getTransactionList} from "../axios.config";

export default function HistoryPage() {
    // getTransactionList()

    return (
        <Box style={{padding: "2%"}}>
            <CollapsibleTable/>
        </Box>
    )
}