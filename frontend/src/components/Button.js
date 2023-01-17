import React from "react";
import { Button } from "@mui/material";

export default function MangoButton(props){
    return (
        <Button     
            style={{
                    backgroundColor: "#FFC107",
                    color: "black"
                }}>{props.children}</Button>
    )
}