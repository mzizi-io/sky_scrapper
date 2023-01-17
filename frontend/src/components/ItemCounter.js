import React from "react";
import styled from "styled-components";
import { Button } from "@mui/material";
import { IoMdAddCircle } from 'react-icons/io';
import { AiFillMinusCircle } from 'react-icons/ai';
import { useState } from "react";

export default function ItemCounter(){
    const [counter, setCounter] = useState(0)

    function IncNum(){
        setCounter(counter + 1)
    }

    function DecNum(){
        setCounter(Math.max(0, counter - 1))
    }

    return (
        <CounterContainer>
            <Button style={{ color: "#FFC107" }} size = "large" onClick={IncNum}>
                <IoMdAddCircle />
            </Button>

            <h5>{ counter }</h5>

            <Button style={{ color: "#FFC107" }} size = "large" onClick={DecNum}>
                <AiFillMinusCircle />
            </Button>
      </CounterContainer>
    )
}

const CounterContainer = styled.div`
    display: flex;
`