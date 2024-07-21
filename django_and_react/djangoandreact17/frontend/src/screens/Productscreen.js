import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import {
  Row,
  Col,
  Image,
  ListGroup,
  Button,
  Card,
  Form,
  ListGroupItem,
  FormLabel,
  FormGroup,
  FormControl,
} from "react-bootstrap";
import Rating from "../components/Rating";

import {
  listproductdetails,
  createproductreview,
} from "../actions/productactions";
import { useDispatch, useSelector } from "react-redux";
import { productcreatereviewreset } from "../constants/productconstants";

const Productscreen = (props) => {
  const [qty, setqty] = useState(1);
  const [rating, setrating] = useState(0);
  const [comment, setcomment] = useState("");
  const dispatch = useDispatch();
  const productdetail = useSelector((state) => state.productdetail);
  const { product, } = productdetail;
 
  const userlogin = useSelector((state) => state.userlogin);
  const { userinfo } = userlogin;

  const productcreatereview = useSelector((state) => state.productcreatereview);
  const {
    loading: loadingproductreview,
    error: errorproductreview,
    success: successproductreview,
  } = productcreatereview;
 

  const addtocarthandler = () => {
    props.history.push(`/cart/${props.match.params.id}?qty=${qty}`);
  };
  const reviewonsubmithandler = (e) => {
    e.preventDefault()
    dispatch(createproductreview(props.match.params.id,{rating,comment}))
 
  };
  useEffect(() => {
    if (successproductreview) {
      setrating(0);
      setcomment("");
      dispatch({ type: productcreatereviewreset });
    }
    dispatch(listproductdetails(props.match.params.id));
  }, [dispatch, props.match, successproductreview]);
  return (
    <div>
      <Link to="/" className="btn btn-light my-3">
        Go Back
      </Link>
      <div>
        <Row>
          <Col md={6}>
            <Image src={product.image} alt={product.name} fluid />
          </Col>
          <Col md={3}>
            <ListGroup variant="flush">
              <ListGroup.Item>
                <h3>{product.name}</h3>
              </ListGroup.Item>
              <ListGroup.Item>
                {console.log(product.rating)}
                <Rating
                  value={product.rating}
                  text={`${product.numreviews} reviews`}
                  color={"#f8e825"}
                />
              </ListGroup.Item>
              <ListGroup.Item>Price: ${product.price}</ListGroup.Item>
              <ListGroup.Item>
                Description: ${product.description}
              </ListGroup.Item>
            </ListGroup>
          </Col>
          <Col md={3}>
            <Card>
              <ListGroup variant="flush">
                <ListGroup.Item>
                  <Row>
                    <Col>Price:</Col>
                    <Col>
                      <strong>${product.price}</strong>
                    </Col>
                  </Row>
                </ListGroup.Item>
                <ListGroup.Item>
                  <Row>
                    <Col>Status:</Col>
                    <Col>
                      <strong>
                        {product.countinstocks > 0
                          ? "In stock"
                          : "out of stuck"}
                      </strong>
                    </Col>
                  </Row>
                </ListGroup.Item>
                {product.countinstocks > 0 && (
                  <ListGroup.Item>
                    <Row>
                      <Col>Qty</Col>
                      <Col xs="auto" className="m1-1">
                        <Form.Control
                          as="select"
                          value={qty}
                          onChange={(e) => setqty(e.target.value)}
                        >
                          {[...Array(product.countinstocks).keys()].map((x) => (
                            <option key={x + 1}>{x + 1}</option>
                          ))}
                        </Form.Control>
                      </Col>
                    </Row>
                  </ListGroup.Item>
                )}
                <ListGroup.Item>
                  <Button
                    onClick={addtocarthandler}
                    className="btn-block"
                    disabled={!product.countinstocks > 0}
                    type="button"
                  >
                    Add to cart
                  </Button>
                </ListGroup.Item>
              </ListGroup>
            </Card>
          </Col>
        </Row>
        <Row>
          <Col md={6}>
            <h4>Reviews</h4>
            {product.reviews && product.reviews.length === 0 && (
              <h2>no reviews</h2>
            )}
            <ListGroup variant="flush">
              {product.reviews &&
                product.reviews.map((review) => (
                  <ListGroupItem key={review._id}>
                    <strong>{review.name}</strong>
                    <Rating value={review.rating} color="#f8e825" />
                    <p>{review.createdat.substring(0, 10)}</p>
                    <p>{review.comment}</p>
                  </ListGroupItem>
                ))}
              <ListGroupItem>
                <h4>Write a review</h4>
                {loadingproductreview && <h4>loading...</h4>}
                {successproductreview && <h4>review submited</h4>}
                {errorproductreview && <h4>{errorproductreview}</h4>}
                {userinfo ? (
                  <Form onSubmit={reviewonsubmithandler}>
                    <FormGroup>
                      <FormLabel>rating</FormLabel>
                      <FormControl
                        as="select"
                        value={rating}
                        onChange={(e) => setrating(e.target.value)}
                      >
                        <option value="">Select...</option>
                        <option value="1">1-poor</option>
                        <option value="2">2-fair</option>
                        <option value="3">3-good</option>
                        <option value="4">4-very good</option>
                        <option value="5">5-excellent</option>
                      </FormControl>
                    </FormGroup>
                    <FormGroup controlId="comment">
                      <FormLabel>review</FormLabel>
                      <FormControl
                        as="textarea"
                        rows="5"
                        value={comment}
                        onChange={(e) => setcomment(e.target.value)}
                      ></FormControl>
                    </FormGroup>
                    <Button
                      // diasbled={loadingproductreview}
                      type="submit"
                      variant="primary"
                    >
                      Submit
                    </Button>
                  </Form>
                ) : (
                  <h2 variant="info">
                    please <Link to="/">login</Link> to write a review
                  </h2>
                )}
              </ListGroupItem>
            </ListGroup>
          </Col>
        </Row>
      </div>
    </div>
  );
};

export default Productscreen;
