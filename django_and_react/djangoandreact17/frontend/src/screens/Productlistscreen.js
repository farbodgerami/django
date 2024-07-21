import React, { useEffect } from "react";

import { Button, Row, Col, Table } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import {
  listproducts,
  deleteproduct,
  createproduct,
} from "../actions/productactions";
import Paginate from '../components/paginate'
import { LinkContainer } from "react-router-bootstrap";
import { productcreatereset } from "../constants/productconstants";
const Productlistscreen = ({ history, match }) => {
  const dispatch = useDispatch();

  const productlist = useSelector((state) => state.productlist);
  const { loading, error, products,page,pages } = productlist;
 
  const userlogin = useSelector((state) => state.userlogin);
  const { userinfo } = userlogin;

  const productcreate = useSelector((state) => state.productcreate);
  const {
    loading: loadingcreate,
    error: errorcreate,
    success: successcreate,
    product: createdproduct,
  } = productcreate;

  const productdelete = useSelector((state) => state.productdelete);

  const {
    loading: loadingdelete,
    error: errordelete,
    success: successdelete,
  } = productdelete;

  const deletehandler = (id) => {
    if (window.confirm("mikhai pakesh koni?")) {
      dispatch(deleteproduct(id));
    }
  };

  let keyword = history.location.search;
  useEffect(() => {
    dispatch({ type: productcreatereset });

    if (!userinfo || !userinfo.isadmin) {
      history.push("/login");
    }
    if (successcreate) {
      history.push(`/admin/product/${createdproduct._id}/edit`);
    } else {
      dispatch(listproducts(keyword));
    }
  }, [
    dispatch,
    history,
    userinfo,
    successdelete,
    successcreate,
    createdproduct,keyword
  ]);
  const createproducthandler = () => {
    dispatch(createproduct());
  };
  return (
    <div>
      <Row className="align-items-center">
        <Col>
          <h1>Products</h1>
        </Col>
        <Col className="text-right">
          <Button className="text-right" onClick={createproducthandler}>
            <i className="fas fa-plus"></i>
            create Product
          </Button>
        </Col>
      </Row>
      {loadingdelete && <h1>loading...</h1>}
      {errordelete && <h1>{errordelete}</h1>}

      {loadingcreate && <h1>loading...</h1>}
      {errorcreate && <h1>{errorcreate}</h1>}

      {/* agha tarkibiro dashte bash: */}
      {loading ? (
        <h1>loading...</h1>
      ) : error ? (
        <h1>{error}</h1>
      ) : (
        <div>

        <Table striped bordered hover responsive className="table-small">
          <thead>
            <tr>
              <th>ID</th>
              <th>NAME</th>
              <th>PRICE</th>
              <th>BRAND</th>
            </tr>
          </thead>
          {products.map((product) => (
            <tr key={product._id}>
              <td>{product._id}</td>
              <td>{product.name}</td>
              <td>{product.price}</td>
              <td>{product.brand}</td>
              <td>{product.catecory}</td>
              <td>
                <LinkContainer
                  variant="light"
                  className="btn-sm"
                  to={`/admin/product/${product._id}/edit`}
                >
                  <Button>
                    <i className="fas fa-edit">edit</i>
                  </Button>
                </LinkContainer>
                <Button
                  variant="lisht"
                  className="btn-sm"
                  onClick={() => deletehandler(product._id)}
                >
                  <i className="fas fa-trash" style={{ color: "red" }}>
                    delete
                  </i>
                </Button>
              </td>
            </tr>
          ))}
        </Table>
         
        <Paginate page={page} pages={pages} keyword={keyword} isadmin={true} />
        </div>
      )}
    </div>
  );
};

export default Productlistscreen;
