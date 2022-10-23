import React from 'react'
import { useLocation, Navigate, Outlet } from "react-router-dom"
import SidebarNav from './SidebarNav'

import { Container, Header, Sidebar, Sidenav, Content, Navbar, Nav } from 'rsuite';
import TopNavBar from './TopNavBar';
const MainLayout = () => {
  return (
    <>
      <Container>
        <SidebarNav />

        <Container>
          <Header>
            <TopNavBar />
          </Header>
          <Content>
            <Outlet />
          </Content>
        </Container>
      </Container>
    </>
  )
}

export default MainLayout