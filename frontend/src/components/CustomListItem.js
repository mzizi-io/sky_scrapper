import React from "react";
import styled from "styled-components";
import { ListItem } from "@mui/material";
import ItemCounter from "./ItemCounter";

export default function CustomListItem(props){
    return(
        <ListItem>                     
            <ListItemContent>{props.children}</ListItemContent> 
            <ItemCounter></ItemCounter>
        </ListItem>
    )
}

const ListItemContent = styled.div`
    width: 5vw;
`