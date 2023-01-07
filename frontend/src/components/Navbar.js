import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';
import Logo from "../assets/img/logo.jpg";

function Navbar(){
    return (
        <NavbarContainer>
            <LogoImage className="logo-container" src ={Logo}/>
            <Navigation> 
                <StyledLink to = {{pathname: "/"}}>Home</StyledLink>
                <StyledLink to = {{pathname: "/about"}}>About</StyledLink>
            </Navigation>
        </NavbarContainer>
    )

}

const LogoImage = styled.img`
    height: 7vh;
    width: 7vh;
    margin-left: 3vw;
    border-radius: 10px;
    z-index: 10;

    &:hover{
        height: 4.5rem;
        width: 4.5rem;
    }
` 

const NavbarContainer = styled.div`
    height: 5rem;
    width: 100vw;
    display: flex;
    align-items: center;
    gap: 55vw;
    z-index: 10;
`

const Navigation = styled.div`
    height: 4rem;
    width: 30vw;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    z-index: 10;
`

const StyledLink = styled(Link)`
    color:  #154360;
    text-decoration: none;
    font-size: 20px;
    font-weight: 600;
    position: relative;
    
    &:hover{
        color: #E55B13;
    }
`

export default Navbar;