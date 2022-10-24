import React from 'react'
import { Grid, Row, Col, Container, Panel, Placeholder } from 'rsuite';

const Pos = () => {
    return (
        <>
            <Container>
               
                    <Row className="show-grid">
                        <Col xs={14}>
                            <Panel header="Panel title" shaded>
                                <Placeholder.Paragraph />
                            </Panel>
                        </Col>
                        <Col xs={10}>
                            <Panel shaded>
                                <Placeholder.Paragraph />
                            </Panel>
                        </Col>
                    </Row>
                
            </Container>
        </>
    )
}

export default Pos