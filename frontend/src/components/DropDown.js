import React, {useState} from 'react';
import Dropdown from 'react-bootstrap/Dropdown';
import styled from 'styled-components';
import DropdownItem from 'react-bootstrap/esm/DropdownItem';
import DropdownMenu from 'react-bootstrap/esm/DropdownMenu';

function DropDown(props) {
  {/* Handling state */}
  const [title, setTitle] = useState(props.title)

  const changeHeader = function(e){
    const value = e.target.innerHTML
    setTitle(value)
  }

  
  const optionsList = props.options.split(" ")
  const menuItems = optionsList.map((option) => {
    return <Item href={"#/" + option} key = {option} onClick={changeHeader}>{option}</Item>
  })

  return (
    <Dropdown size="6px">
      <Dropdown.Toggle variant="warning" id="dropdown-basic">
        {title}
      </Dropdown.Toggle>

      <Menu>
          {menuItems}
      </Menu>
    </Dropdown>
  );
}

const Item = styled(DropdownItem)`
  background-color: #fff;
`

const Menu = styled(DropdownMenu)`
  background-color: #fff;
`

export default DropDown;