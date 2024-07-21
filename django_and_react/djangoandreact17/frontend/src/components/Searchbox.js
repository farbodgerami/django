import React, { useState } from "react";
import { Button, Form, FormControl } from "react-bootstrap";
import { useHistory } from "react-router-dom";

const Searchbox = ( ) => {
  const [keyword, setkeyword] = useState("");
  let history=useHistory()
  const submithandler = (e) => {
    e.preventDefault();
if(keyword){history.push(`/?keyword=${keyword}&page=1`)}else{history.push(history.location.pathname)}
  }; 
 
  return (
    <Form onSubmit={submithandler} style={{display:'flex'}}  >
       
        <FormControl
          type="text"
          name="q"
          onChange={(e) => setkeyword(e.target.value)}
          className="mr-sm-2 ml-sm-5"
        ></FormControl>
        <Button type="submit" variant="outline-success" className="p-2">
          submit
        </Button>
       
    </Form>
  );
};

export default Searchbox;
