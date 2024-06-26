import TextField from "@mui/material/TextField";

export default function SeedGenerator({setSeed}) {
    const numberOfFields = 24

    const handleInputChange = (event) => {
        const {id, value} = event.target;
        setSeed((prevValues) => ({
            ...prevValues,
            [id]: value,
        }));
    };

    return (
        <>
            {Array.from({length: numberOfFields}, (_, index) => (
                <TextField key={index} label={`Cлово ${index + 1}`} variant="outlined" onChange={handleInputChange}/>
            ))}
        </>
    )
}