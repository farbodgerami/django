import {
  userloginfail,
  userloginrequest,
  userloginsuccess,
  userlogout,
  userregisterfail,
  userregisterrequest,
  userregistersuccess,
  userdetailsfail,
  userdetailsrequest,
  userdetailssuccess,
  userupdateprofilefail,
  userupdateprofilerequest,
  userupdateprofilesuccess,
  userdetailsreset,
  userlistfail,
  userlistrequest,
  userlistreset,
  userlistsuccess,
  userdeletefail,
  userdeleterequest,
  userdeletesuccess,
  userupdatefail,
  userupdaterequest,
  userupdatesuccess,
} from "../constants/userconstants";
import axios from "axios";

export const login = (email, password) => {
  return async (dispatch) => {
    try {
      dispatch({ type: userloginrequest });
      const config = { headers: { "Content-type": "application/json" } };
      const { data } = await axios.post(
        "/users/login",
        { username: email, password: password },
        config
      );
      dispatch({ type: userloginsuccess, payload: data });
      localStorage.setItem("userinfo", JSON.stringify(data));
    } catch (error) {
      dispatch({
        type: userloginfail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};

export const logout = () => {
  return async (dispatch) => {
    localStorage.removeItem("userinfo");
    dispatch({ type: userlogout });
    dispatch({ type: userdetailsreset });
    dispatch({ type: userlistreset });
  };
};

export const register = (name, email, password) => {
  return async (dispatch) => {
    try {
      dispatch({ type: userregisterrequest });
      const config = { headers: { "Content-type": "application/json" } };
      const { data } = await axios.post(
        "/users/register/",
        { name: name, email: email, password: password },
        config
      );

      dispatch({ type: userregistersuccess, payload: data });
      // hall ke register kardim ba hamoon login mikonim:
      dispatch({ type: userloginsuccess, payload: data });
      localStorage.setItem("userinfo", JSON.stringify(data));
    } catch (error) {
      dispatch({
        type: userregisterfail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};
export const getuserdetails = (id) => {
  return async (dispatch, getState) => {
    try {
      dispatch({ type: userdetailsrequest });
      const {
        userlogin: { userinfo },
      } = getState();
      const config = {
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${userinfo.token}`,
        },
      };
    
      const response = await axios.get(`/users/${id}`, config);
      const data=response.data

      dispatch({ type: userdetailssuccess, payload: data });
    } catch (error) {
    
      dispatch({
        type: userdetailsfail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};

export const updateuserprofile = (user) => {
  return async (dispatch, getState) => {
    try {
      dispatch({ type: userupdateprofilerequest });
      const {
        userlogin: { userinfo },
      } = getState();
      const config = {
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${userinfo.token}`,
        },
      };
      const { data } = await axios.post(`/users/profile/update`, user, config);
      dispatch({ type: userupdateprofilesuccess, payload: data });
      dispatch({ type: userloginsuccess, payload: data });
      localStorage.setItem("userinfo", JSON.stringify(data));
    } catch (error) {
      dispatch({
        type: userupdateprofilefail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};

export const listusers = () => {
  return async (dispatch, getState) => {
    try {
      dispatch({ type: userlistrequest });
      const {
        userlogin: { userinfo },
      } = getState();
      const config = {
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${userinfo.token}`,
        },
      };
      const { data } = await axios.get(`/users/`, config);

      dispatch({ type: userlistsuccess, payload: data });
    } catch (error) {
      dispatch({
        type: userlistfail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};

export const deleteusers = (id) => {
  return async (dispatch, getState) => {
    try {
      dispatch({ type: userdeleterequest });
      const {
        userlogin: { userinfo },
      } = getState();
      const config = {
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${userinfo.token}`,
        },
      };
      const { data } = await axios.delete(`/users/delete/${id}`, config);

      dispatch({ type: userdeletesuccess, payload: data });
    } catch (error) {
      dispatch({
        type: userdeletefail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};

export const updateusers = (user) => {
  return async (dispatch, getState) => {
    try {
      dispatch({ type: userupdaterequest });
      const {
        userlogin: { userinfo },
      } = getState();
      const config = {
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${userinfo.token}`,
        },
      };
      const { data } = await axios.post(
        `/users/update/${user._id}/`,
        user,
        config
      );

      dispatch({ type: userupdatesuccess });
      dispatch({ type: userdetailssuccess, payload: data });
    } catch (error) {
      dispatch({
        type: userupdatefail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};
