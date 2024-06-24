import CollapsibleTable from "../components/table";
import Box from "@mui/material/Box";
import {getWallets} from "../axios.config";


export default function WalletsPage() {
    // console.log(getWallets())
    return (
        <Box style={{padding: "2%"}}>
            <CollapsibleTable/>
        </Box>
    )
}