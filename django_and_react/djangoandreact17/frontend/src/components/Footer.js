import React from "react";
import { Container, Row, Col } from "react-bootstrap";
const Footer = () => {
  return (
    <div>
      <Container>
        <Row>
            <Col className='text-center py-3'>
            Copyright &copy; ProShop</Col>
        </Row>
      </Container>
    </div>
  );
};

export default Footer;
