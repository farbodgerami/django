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
import { login } from "../actions/useractions";
import Formcontainer from "../components/Formcontainer";

const Loginscreen = ({location,history}) => {
  const dispatch=useDispatch()
  const [email, setemail] = useState("");
  const [password, setpassword] = useState("");
  const redirect=location.search ? location.search.split('=')[1]:'/'
  const userlogin=useSelector(state=>state.userlogin)
  const {error,loading,userinfo}=userlogin
  useEffect(()=>{
 
    if(userinfo){
      history.push(redirect)
    }
  },[history,userinfo,redirect])
  const submithandeler=(e)=>{e.preventDefault();dispatch(login(email,password))}
  return (
 
    <Formcontainer>
      <h1>Sign In</h1>
      {error&&<h1>{error}</h1> }
      {loading&&<h1>loading...</h1> }
      <Form onSubmit={submithandeler}>
        <FormGroup controlId="email">
          <FormLabel>Email Address</FormLabel>
          <FormControl
            type="email"
            placeholder="enter email"
            value={email}
            onChange={(e) => setemail(e.target.value)}
          ></FormControl>
        </FormGroup>
        <FormGroup controlId="password">
          <FormLabel>Password</FormLabel>
          <FormControl
            type="Password"
            placeholder="enter Password"
            value={password}
            onChange={(e) => setpassword(e.target.value)}
          ></FormControl>
        </FormGroup>
        <Button type='submit' variant='primary'>Sign In</Button>
      </Form>
      <Row className='py-3'>
          <Col>new Customer?<Link to={'/register'}>Register</Link></Col>
      </Row>
    </Formcontainer>
  );
};

export default Loginscreen;
