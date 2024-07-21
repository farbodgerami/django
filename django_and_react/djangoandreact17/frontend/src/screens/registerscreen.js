import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import {
  Form,
  Button,
  Row,
  Col,
  FormGroup,
  FormLabel,
  FormControl,
} from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { register } from "../actions/useractions";
import Formcontainer from "../components/Formcontainer";

const Registerscreen = ({ location, history }) => {
  const dispatch = useDispatch();
  const [name, setname] = useState("");
  const [email, setemail] = useState("");
  const [password, setpassword] = useState("");
  const [confirmpassword, setconfirmpassword] = useState("");
  const [message, setmessage] = useState("");
  const userregister = useSelector((state) => state.userregister);
  const { error, loading, userinfo } = userregister;
  const redirect = location.search ? location.search.split("=")[1] : "/";
  useEffect(() => {
    if (userinfo) {
      history.push(redirect);
    }
  }, [history, userinfo, redirect]);
  const submithandeler = (e) => {
    e.preventDefault();
    if(password!==confirmpassword){setmessage('passwords do not match')}else{
        dispatch(register(name,email,password))
    }
    dispatch(register(name,email,password));
  };
  return  <Formcontainer>
  <h1>Sign Up</h1>
  {message&&<h1>{message}</h1>}
  {error&&<h1>{error}</h1> }
  {loading&&<h1>loading...</h1> }
  <Form onSubmit={submithandeler}>
    <FormGroup controlId="name">
      <FormLabel>Name</FormLabel>
      <FormControl
        type="text"
        required
        placeholder="enter name"
        value={name}
        onChange={(e) => setname(e.target.value)}
      ></FormControl>
    </FormGroup>

    <FormGroup controlId="email">
      <FormLabel>Email Address</FormLabel>
      <FormControl
        type="email"
        required
        placeholder="enter email"
        value={email}
        onChange={(e) => setemail(e.target.value)}
      ></FormControl>
    </FormGroup>

    <FormGroup controlId="password">
      <FormLabel>Password</FormLabel>
      <FormControl
      required
        type="Password"
        placeholder="enter Password"
        value={password}
        onChange={(e) => setpassword(e.target.value)}
      ></FormControl>
    </FormGroup>

    <FormGroup controlId="confirmpassword">
      <FormLabel>ConfirmPassword</FormLabel>
      <FormControl
      required
        type="Password"
        placeholder="confirm Password"
        value={confirmpassword}
        onChange={(e) => setconfirmpassword(e.target.value)}
      ></FormControl>
    </FormGroup>

    <Button type='submit' variant='primary'>Register</Button>
  </Form>
  <Row className='py-3'>
      <Col>have an account?<Link to={'/login'}>Sign In</Link></Col>
  </Row>
</Formcontainer>
};

export default Registerscreen;
