import React, { useEffect } from "react";
import { Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import {
  Row,
  Col,
  ListGroup,
  Image,
  Form,
  Button,
  Card,
  ListGroupItem,
} from "react-bootstrap";

import { addtocart,removefromdart } from "../actions/cartactions";
const Cartscreen = ({ match, location, history }) => {
  const productid = match.params.id;
  const qty = location.search ? Number(location.search.split("=")[1]) : 1;

  const dispatch = useDispatch();
  const cart = useSelector((state) => state.cart);
  const { cartitems } = cart;
  const removefromcarthandler = (id) => {
    console.log("remove:", id);dispatch(removefromdart(id))
  };
  const checkouthandler=()=>{history.push('/login?redirect=shipping')}

  useEffect(() => {
    if (productid) {
      dispatch(addtocart(productid, qty));
    }
  }, [dispatch, productid, qty]);
  return (
    <Row>
      <Col md={8}>
        <h1>Shopping Cart</h1>
        {cartitems.length === 0 ? (
          <h1>
            cart is empty<Link to="/">go back</Link>
          </h1>
        ) : (
          <ListGroup variant="flush">
            {cartitems.map((item) => (
              <ListGroup.Item key={item.product}>
                <Row>
                  <Col md={2}>
                    <Image src={item.image} alt={item.name} fluid rounded />
                  </Col>
                  <Col md={3}>
                    <Link to={`/product/${item.product}`}>{item.name}</Link>
                  </Col>
                  <Col md={2}>${item.price}</Col>
                  <Col md={3}>
                    <Form.Control
                      as="select"
                      value={item.qty}
                      onChange={(e) =>
                        dispatch(
                          addtocart(item.product, Number(e.target.value))
                        )
                      }
                    >
                      {[...Array(item.countinstocks).keys()].map((x) => (
                        <option key={x + 1}>{x + 1}</option>
                      ))}
                    </Form.Control>
                  </Col>
                  <Col md={1}>
                    <Button type="button" variant="light">
                      <i
                        className="fas fa-trash"
                        onClick={() => removefromcarthandler(item.product)}
                      >
                        trashicon
                      </i>
                    </Button>
                  </Col>
                </Row>
              </ListGroup.Item>
            ))}
          </ListGroup>
        )}
      </Col>

      <Col md={4}>
        <Card>
          <ListGroup variant="flush">
            <ListGroupItem>
              <h2>
                subtotal ({cartitems.reduce((acc, item) => acc + item.qty, 0)})
              </h2>
              $
              {cartitems
                .reduce((acc, item) => acc + item.qty * item.price, 0)
                .toFixed(2)}
            </ListGroupItem>
          </ListGroup>
          <ListGroupItem>
            <Button type='button' className='btn-block' disabled={cartitems.length===0} onClick={checkouthandler}>
              proceed to checkout
            </Button>
          </ListGroupItem>
        </Card>
      </Col>
    </Row>
  );
};

export default Cartscreen;
