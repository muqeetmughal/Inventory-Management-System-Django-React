import React from 'react'
import { Navbar, Nav } from 'rsuite';
import HomeIcon from '@rsuite/icons/legacy/Home';
import Gear from '@rsuite/icons/legacy/Gear';
import { Link } from 'react-router-dom';

const TopNavBar = () => {
    return (
        <div>
            <Navbar>
                {/* <Navbar.Brand href="#">RSUITE</Navbar.Brand> */}
                <Nav>
                    {/* <Nav.Item icon={<HomeIcon />}>
                        <Link to={"/"}>
                            Home
                        </Link>
                    </Nav.Item>
                    <Nav.Item>
                        <Link to={"/users"}>
                            Users
                        </Link>
                    </Nav.Item>
                    <Nav.Item>
                    <Link to={"/users/add"}>
                            Add User
                        </Link>
                    </Nav.Item>
                    <Nav.Menu title="About">
                        <Nav.Item>Company</Nav.Item>
                        <Nav.Item>Team</Nav.Item>
                        <Nav.Menu title="Contact">
                            <Nav.Item>Via email</Nav.Item>
                            <Nav.Item>Via telephone</Nav.Item>
                        </Nav.Menu>
                    </Nav.Menu> */}
                </Nav>
                <Nav pullRight>
                    <Nav.Item icon={<Gear />}>Logout</Nav.Item>
                </Nav>
            </Navbar>
        </div>
    )
}

export default TopNavBar