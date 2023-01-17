import React from "react";
import styled from "styled-components"
import { MdLuggage } from "react-icons/md";
import { BsPersonCheckFill} from "react-icons/bs";

import DropdownButton from "./DropDown";
import CountrySelect from "./CountrySelect";
import BaseDatePicker from "./DatePicker";

import JumboVideoWebm from "../assets/video/video.webm"
import JumboVideoMP4 from "../assets/video/video.mp4"
import JumboVideoOGV from "../assets/video/video.ogv"
import Styles from "../assets/css/main.css"
import MangoButton from "./Button";
import DropDownDiv from "./DropDownDiv";
import ChildrenAndBaggageDiv from "./ChildrenAndBaggage";

function Jumbotron(){
    return (
        <JumbotronContainer>
            <SelectionModal>
                <SelectionHeaderParameters>
                    <DropdownButton title='Return' options="Return One-Way Nomad" ></DropdownButton>
                    <DropdownButton title='Economy' options="Economy Business First" ></DropdownButton>
                    <DropDownDiv id="baggage-passengers" height="5" width="7" dropDownContent = { <ChildrenAndBaggageDiv/> } >
                        <pre><BsPersonCheckFill size={30}/> &emsp; <MdLuggage size={30}/></pre>
                    </DropDownDiv>
                </SelectionHeaderParameters>

                <SelectionContainer>
                    <CountrySelect label="Departure"/>
                    <CountrySelect label="Arrival"/>
                    <BaseDatePicker label="From"/>
                    <BaseDatePicker label="To"/>
                    <MangoButton variant="contained"> Find flights</MangoButton>
                </SelectionContainer>
            </SelectionModal>

            {/* Used this instead of styled components because of issues loading video */}
            <video style={Styles} preload="true" autoPlay = "autoplay" muted={true}>
                <source src={JumboVideoMP4} type="video/mp4"/>
                <source src={JumboVideoOGV} type="video/ogg"/>
                <source src={JumboVideoWebm} type="video/webm"/>
            </video>

        </JumbotronContainer>
    )
}

const JumbotronContainer = styled.div`
    height: 20vh;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: -10;
    overflow: visible;
`

const SelectionModal = styled.div`
    height: 20vh;
    width: 70vw;
    border-radius: 15px;
    position: absolute;
    top: 25vh;
    background-color: white;
    box-shadow: rgba(37, 42, 49, 0.4) 0px 4px 12px 0px;
    border: 1px solid #cccccc;
    padding: 10px;
    z-index: 0;
`

const SelectionHeaderParameters = styled.div`
    height: 30%;
    display: flex;
    align-items: center;
    gap: 1vw;
    margin-left: 2vw;
    margin-top: 0.5vw;
    `

const SelectionContainer = styled.div`
    height: 60%;
    display: flex;
    align-items: center;
    gap: 0.5vw;
    padding-left: 2vw;
    padding: 0 3vh 0vh 3vh;
`

export default Jumbotron;