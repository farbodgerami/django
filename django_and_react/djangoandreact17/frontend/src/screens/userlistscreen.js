import React, {   useEffect } from "react";
import { Button, Table,} from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { listusers, deleteusers } from "../actions/useractions";
import { userdetailsreset } from "../constants/userconstants";
import { LinkContainer } from "react-router-bootstrap";
const Userlistscreen = ({ history }) => {
  const dispatch = useDispatch();
  dispatch({type:userdetailsreset})
 
  const userlist = useSelector((state) => state.userlist);
  const { loading, error, users } = userlist;
  const userlogin = useSelector((state) => state.userlogin);
  const { userinfo } = userlogin;

  const userdelete = useSelector((state) => state.userdelete);
  const { success: successdelete } = userdelete;

  const deletehandler = (id) => {
    if (window.confirm("mikhai pakesh koni?")) {
      dispatch(deleteusers(id));
    }
  };

  useEffect(() => {
  // besyar ajib ast ke dispatch({type:userdetailsreset}) dar
  //inja kar mikonad vali asar nemigozarad...!!!
   
    if (userinfo && userinfo.isadmin) {
      dispatch(listusers());
    } else {
      history.push("/login");
    }
  }, [dispatch, history, successdelete,userinfo]);
  return (
    <div>
      <h1>users</h1>
      {/* agha tarkibiro dashte bash: */}
      {loading ? (
        <h1>loading...</h1>
      ) : error ? (
        <h1>{error}</h1>
      ) : (
        <Table striped bordered hover responsive className="table-small">
          <thead>
            <tr>
              <th>ID</th>
              <th>NAME</th>
              <th>EMAIL</th>
              <th>ADMIN</th>
            </tr>
          </thead>
          {users.map((user) => (
            <tr key={user._id}>
              <td>{user._id}</td>
              <td>{user.name}</td>
              <td>{user.email}</td>
              <td>
                {user.isadmin ? (
                  <i className="fas fa-ckeck" style={{ color: "green" }}>
                    hast
                  </i>
                ) : (
                  <i className="fas fa-ckeck" style={{ color: "red" }}>
                    nist
                  </i>
                )}
              </td>
              <td>
                <LinkContainer
                  variant="light"
                  className="btn-sm"
                  to={`/admin/user/${user._id}/edit`}
                >
                  <Button>
                    <i className="fas fa-edit">edit</i>
                  </Button>
                </LinkContainer>
                <Button
                  variant="lisht"
                  className="btn-sm"
                  onClick={() => deletehandler(user._id)}
                >
                  <i className="fas fa-trash" style={{ color: "red" }}>
                    delete
                  </i>
                </Button>
              </td>
            </tr>
          ))}
        </Table>
      )}
    </div>
  );
};

export default Userlistscreen;
