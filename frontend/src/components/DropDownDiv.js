import React, { useEffect, useState } from "react";
import styled from "styled-components";

export default function DropDownDiv(props){
    const [visibility, setVisibility] = useState("hidden")

    const handleClick = function(){
        // Change hidden property on div
        if (visibility === "hidden"){
            setVisibility("visible")
        }else{
            setVisibility("hidden")
        } 
    }

    
    useEffect(() => {
        document.addEventListener("mousedown", (e) =>{
            /* Check if the dropdown div contains the element */
            const dropdownItems = document.getElementsByClassName("dropdown")
            console.log(dropdownItems)
            dropdownItems.map((item) => { return e.target === item})
            console.log(e.target)
            console.log(dropdownItems)
        })
    })

    return(
        <div>
            <DropDown className="dropdown" height= {props.height} width={props.width} onClick = {handleClick} >{props.children}</DropDown>
            <DropdownContent visibility = { visibility }>{props.dropDownContent}</DropdownContent>
        </div>
    )
}

const DropDown = styled.div`
    border-radius: 5px;
    height: ${props => props.height.concat("vh")};
    width: ${props => props.width + "vw"};
    display: flex;
    justify-content: center;
    align-items: center;
    padding-top: 2vh;
    border: 1px solid #ebe0d6;

    &:hover{
        background-color: #ebe0d6;
        cursor: pointer;
    }
`

const DropdownContent = styled.div`
    background-color: #fff;
    height: 40vh;
    width: 15vw;
    border: 1px solid black;
    visibility: ${ props => props.visibility };
    position: absolute;
    z-index: 2;
`