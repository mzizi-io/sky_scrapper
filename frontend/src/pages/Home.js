import React from "react";
import Navbar from "../components/Navbar";
import Jumbotron from "../components/Jumbotron";

function Home(){
    return(
        <div >
            <Navbar className="navbar"></Navbar>
            <Jumbotron className="jumbotron"></Jumbotron>
        </div>
    )
}


export default Home;