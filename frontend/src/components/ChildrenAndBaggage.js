import React from "react";
import styled from "styled-components";
import List from '@mui/material/List';
import CustomListItem from "./CustomListItem";

export default function ChildrenAndBaggageDiv(){
    return (
        <div>
            <Header> Passengers</Header>
            <List>
                <CustomListItem>Adults</CustomListItem>                   
                <CustomListItem>Children</CustomListItem>
            </List>

            <Header>Baggage</Header>
            <List>                    
                <CustomListItem>Check-In Baggage</CustomListItem>
                <CustomListItem>Hand Luggage</CustomListItem>
            </List>
        </div>
    )
}

const Header = styled.div`
    font-weight: 600;
    margin-left: 0.5vw;
    margin-top: 0.5vw;

    &:hover{
        background-color: #ebe0d6;
        cursor: pointer;
    }
`