import React from 'react'
import { useLocation, Navigate, Outlet } from "react-router-dom"
import SidebarNav from './SidebarNav'
import HomeIcon from '@rsuite/icons/legacy/Home';
import CogIcon from '@rsuite/icons/legacy/Cog';

import { Container, Header, Sidebar, Footer, Content, Navbar, Nav } from 'rsuite';
import TopNavBar from './TopNavBar';
const POSLayout = () => {
  return (
    <>
      <Container>
        <Header>
          <Navbar appearance="inverse">
            <Navbar.Brand>
              <a style={{ color: '#fff' }}>Brand</a>
            </Navbar.Brand>
            <Nav>
              <Nav.Item icon={<HomeIcon />}>Home</Nav.Item>
              <Nav.Item>News</Nav.Item>
              <Nav.Item>Products</Nav.Item>
              <Nav.Menu title="About">
                <Nav.Item>Company</Nav.Item>
                <Nav.Item>Team</Nav.Item>
                <Nav.Item>Contact</Nav.Item>
              </Nav.Menu>
            </Nav>
            <Nav pullRight>
              <Nav.Item icon={<CogIcon />}>Settings</Nav.Item>
            </Nav>
          </Navbar>
        </Header>
        <Content><Outlet /></Content>
        <Footer>Footer</Footer>
      </Container>
    </>
  )
}

export default POSLayout