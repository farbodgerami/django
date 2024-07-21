import React, { useState, useEffect } from "react";

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
import { getuserdetails, updateuserprofile } from "../actions/useractions";

import { userresetprofile } from "../constants/userconstants";
const Profilescreen = ({ location, history }) => {
  const dispatch = useDispatch();
  const [name, setname] = useState("");
  const [email, setemail] = useState("");
  const [password, setpassword] = useState("");
  const [confirmpassword, setconfirmpassword] = useState("");
  const [message, setmessage] = useState("");

  const userdetails = useSelector((state) => state.userdetails);
  const { error, loading, user } = userdetails;

  const userupdateprofile = useSelector((state) => state.userupdateprofile);
  const { success } = userupdateprofile;

  const userlogin = useSelector((state) => state.userlogin);
  const { userinfo } = userlogin;

  useEffect(() => {
    if (!userinfo) {
      history.push("/login");
    } else {
      if (!user || !user.name || success || userinfo._id !== user._id) {
        dispatch({ type: userresetprofile });
        dispatch(getuserdetails("profile"));
      } else {
        setname(user.name);
        setemail(user.email);
      }
    }
  }, [dispatch, history, userinfo, user, success]);
  const submithandeler = (e) => {
    e.preventDefault();
    if (password !== confirmpassword) {
      setmessage("passwords do not match");
      return;
    } else {
      console.log("updating...");
      setmessage("");
    }
    dispatch(
      updateuserprofile({
        id: user._id,
        name: name,
        email: email,
        password: password,
      })
    );
  };
  return (
    <Row>
      <Col md={3}>
        <h2>User Profile</h2>
        <h1>Sign Up</h1>
        {message && <h1>{message}</h1>}
        {error && <h1>{error}</h1>}
        {loading && <h1>loading...</h1>}
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
              type="Password"
              placeholder="enter Password"
              value={password}
              onChange={(e) => setpassword(e.target.value)}
            ></FormControl>
          </FormGroup>

          <FormGroup controlId="confirmpassword">
            <FormLabel>ConfirmPassword</FormLabel>
            <FormControl
              type="Password"
              placeholder="confirm Password"
              value={confirmpassword}
              onChange={(e) => setconfirmpassword(e.target.value)}
            ></FormControl>
          </FormGroup>

          <Button type="submit" variant="primary">
            Update
          </Button>
        </Form>
      </Col>
      <Col md={3}>
        <h2>my orders</h2>
      </Col>
    </Row>
  );
};

export default Profilescreen;
