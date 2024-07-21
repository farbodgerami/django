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
import { getuserdetails, updateusers } from "../actions/useractions";
import Formcontainer from "../components/Formcontainer";
import { userdetailsreset, userupdatereset } from "../constants/userconstants";

const Usereditscreen = ({ match, history }) => {
  const dispatch = useDispatch();
  const userid = match.params.id;
  const [name, setname] = useState("");
  const [email, setemail] = useState("");
  const [isadmin, setisadmin] = useState(false);
  // const [message, setmessage] = useState("");
  const userdetails = useSelector((state) => state.userdetails);
  let { error, loading, user } = userdetails;
  if(user===undefined)  {
  user={}
   history.push("/admin/userlist");
  }
  const userupdate = useSelector((state) => state.userupdate);
  const {
    error: errorupdate,
    loading: loadingupdate,
    success: successupdate,
  } = userupdate;
  useEffect(() => {
    if (successupdate) {
      dispatch({ type: userupdatereset });
      history.push("/admin/userlist");
    } else {
              if (!user.name || user._id !== Number(userid)) {
              dispatch(getuserdetails(userid));
            } else {
                setname(user.name);
                setemail(user.email);
                setisadmin(user.isadmin);   
      }
    }
  }, [user, userid, successupdate, history, dispatch]);

  const submithandeler = (e) => {
    e.preventDefault(); 
    dispatch(updateusers({ _id: user._id, name, email, isadmin }));
  };

  return (
    <div>
      {error ? (
        <div>
          <h1>{error.detail}</h1>
          <Link to="admin/userlist">go back</Link>
        </div>
      ) : (
        <Formcontainer>
          <h1>Edit User</h1>
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

            <FormGroup controlId="email">
              <FormLabel>Email Address</FormLabel>
              <FormControl
                type="email"
                placeholder="enter email"
                value={email}
                onChange={(e) => setemail(e.target.value)}
              ></FormControl>
            </FormGroup>

            <FormGroup controlId="isadmin">
              {/* <Form.Check
              type="checkbox"
              label="is admin"
              
              ckecked={isadmin}
              onChange={(e) => {setisadmin (isadmin );console.log(e.target.value)}}
            ></Form.Check> */}

              <input
                type="checkbox"
                id="checked"
                checked={isadmin}
                onChange={(e) => setisadmin(e.target.checked)}
                name="vehicle1"
              />
              <label> is admin</label>
              <br></br>
            </FormGroup>

            <Button type="submit" variant="primary">
              update
            </Button>
          </Form>
        </Formcontainer>
      )}
    </div>
  );
};

export default Usereditscreen;
