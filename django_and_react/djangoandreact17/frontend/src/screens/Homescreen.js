import React, { useEffect } from "react";
import { Row, Col } from "react-bootstrap";
import { listproducts } from "../actions/productactions";
import Product from "../components/Product";
import { useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import Paginate from "../components/paginate";
import Productcarousel from "../components/productcarousel";
const Homescreen = () => {
  const dispatch = useDispatch();
  const productlist = useSelector((state) => state.productlist);
  let { error, loading, products, page, pages } = productlist;
  let history = useHistory();
  let keyword = history.location.search;

  useEffect(() => {
    dispatch(listproducts(keyword));
  }, [dispatch, keyword]);
  return (
    <div>
      <Productcarousel />
      <h1>Latest Products</h1>
      {loading ? (
        <h2>loading...</h2>
      ) : error ? (
        <h2>{error}</h2>
      ) : (
        <>
          <Row>
            {products.map((product) => (
              <Col sm={12} md={6} lg={3} xl={3} key={product._id}>
                <Product product={product} />
              </Col>
            ))}
          </Row>
          <Paginate page={page} pages={pages} keyword={keyword} />
        </>
      )}
    </div>
  );
};

export default Homescreen;
