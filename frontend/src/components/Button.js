import React from "react";
import styled from "styled-components";

export default function MangoButton(props){
    return (
        <Button>{props.children}</Button>       
    )
}

const Button = styled.button`
    background-color: #FFC107;
    color: black;
    border: 0px;
    border-radius: 5px;
    width: 8vw;
    height: 2vw;
` 