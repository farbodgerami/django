import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import {
  Form,
  Button,
  FormGroup,
  FormLabel,
  FormControl,
} from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { listproductdetails, updateproduct } from "../actions/productactions";
import Formcontainer from "../components/Formcontainer";
import { productupdatereset } from "../constants/productconstants";
import axios from "axios";
const Editproductscreen = ({ match, history }) => {
 
  const dispatch = useDispatch();
  const productid = match.params.id;
  const [name, setname] = useState("");
  const [price, setprice] = useState(0);
  const [file, setfile] = useState();
  const [brand, setbrand] = useState("");
  const [category, setcategory] = useState("");
  const [countinstocks, setcountinstocks] = useState(0);
  const [description, setdescription] = useState("");
  const [uploading, setuploading] = useState(false);

  const productdetail = useSelector((state) => state.productdetail);
  
  const { error, loading, product } = productdetail;

 

  const productupdate = useSelector((state) => state.productupdate);
  const {
    errorupdate,
    loading: loadingupdate,
    success: successupdate,
  } = productupdate;
 

  useEffect(() => {
     
    if (successupdate) {
      dispatch({ type: productupdatereset });
      history.push("/admin/productlist");
    } else {
      if (!product.name || product._id !== Number(productid)) {
   
        dispatch(listproductdetails(productid));
      } else {
        setname(product.name);
        setprice(product.price);
        setbrand(product.brand);
        setcategory(product.category);
        setcountinstocks(product.countinstocks);
        setdescription(product.description);
 
      }
    }
  }, [
    dispatch,
    product,//product dar inja baes mishe ke vaghti joziat az server gerefte shod dakhele form
    // ha gharar begiran
     productid,
      history,
       successupdate,
  ]);
  
  const submithandeler = async (e) => {
    e.preventDefault();
    const formdata = new FormData();
    formdata.append("image", file);
    formdata.append("productid", productid);

     

    setuploading(true);
    try {
      const config = { headers: { "Content-Type": "multipart/form-data" } };
      await axios.post("/products/upload/", formdata, config);

      // setimage(data)
      setuploading(false);
    } catch (error) {
      setuploading(false);
    }
    dispatch(
      updateproduct({
        _id: productid,
        name,
        price,
        brand,
        category,
        countinstocks,
        description,
      })
    );
  };
  const uploadfilehandler = (e) => {
    const file = e.target.files[0];
    setfile(file);
  };
 
  return (
    <div>
      <Link to="/admin/productlist">go back</Link>
      <Formcontainer>
        <h1>Edit Product</h1>
        {loadingupdate && <h1>loading...</h1>}
        {errorupdate && <h1>{errorupdate}</h1>}
        {/* {message && <h1>{message}</h1>} */}
        {error && <h1>{error}</h1>}
        {loading && <h1>loading...</h1>}

        <Form onSubmit={submithandeler}>
          <FormGroup controlId="name">
            <FormLabel>Name</FormLabel>
            <FormControl
              type="text"
              placeholder="enter name"
              value={name}
              onChange={(e) => setname(e.target.value)}
            ></FormControl>
          </FormGroup>

          <FormGroup controlId="price">
            <FormLabel>price</FormLabel>
            <FormControl
              type="number"
              placeholder="enter price"
              value={price}
              onChange={(e) => setprice(e.target.value)}
            ></FormControl>
          </FormGroup>

          <FormGroup controlId="brand">
            <FormLabel>brand</FormLabel>
            <FormControl
              type="text"
              placeholder="enter brand"
              value={brand}
              onChange={(e) => setbrand(e.target.value)}
            ></FormControl>
          </FormGroup>

          <FormGroup controlId="countinstocks">
            <FormLabel>stocks</FormLabel>
            <FormControl
              type="number"
              placeholder="enter stocks"
              value={countinstocks}
              onChange={(e) => setcountinstocks(e.target.value)}
            ></FormControl>
          </FormGroup>

          <FormGroup controlId="category">
            <FormLabel>category</FormLabel>
            <FormControl
              type="text"
              placeholder="enter category"
              value={category}
              onChange={(e) => setcategory(e.target.value)}
            ></FormControl>
          </FormGroup>

          <FormGroup controlId="description">
            <FormLabel>description</FormLabel>
            <FormControl
              type="text"
              placeholder="enter description"
              value={description}
              onChange={(e) => setdescription(e.target.value)}
            ></FormControl>
          </FormGroup>

          <Button type="submit" variant="primary">
            update
          </Button>
        </Form>
      </Formcontainer>
      <form>
        <input type="file" onChange={uploadfilehandler} />
      </form>
    </div>
  );
};

export default Editproductscreen;
