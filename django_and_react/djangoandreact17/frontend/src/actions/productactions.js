import {
  productlistfail,
  productlistrequest,
  productlistsuccess,
  productdetailfail,
  productdetailsuccess,
  productdetailrequest,
  productdeletefail,
  productdeleterequest,
  productdeletesuccess,
  productcreatefail,
  productcreaterequest,
  productcreatesuccess,
  productupdatefail,
  productupdaterequest,
  productupdatesuccess,
  productcreatereviewfail,
  productcreatereviewrequest,
  productcreatereviewsuccess,
  producttoprequest,
  producttopsuccess,
  producttopfail,
} from "../constants/productconstants";
import axios from "axios";
export const listproducts = (keyword = "") => {
  return async (dispatch) => {
    try {
      dispatch({ type: productlistrequest });
     

      const response = await axios.get(`/products${keyword}`);
      console.log("response", response);
      dispatch({ type: productlistsuccess, payload: response.data });
    } catch (error) {
      dispatch({
        type: productlistfail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};

export const listproductdetails = (id) => {
  return async (dispatch) => {
    try {
      dispatch({ type: productdetailrequest });
      const response = await axios.get(`/products/${id}`);
     
      dispatch({ type: productdetailsuccess, payload: response.data });
    } catch (error) {
      dispatch({
        type: productdetailfail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};

export const deleteproduct = (id) => {
  return async (dispatch, getState) => {
    try {
      dispatch({ type: productdeleterequest });
      const {
        userlogin: { userinfo },
      } = getState();
      const config = {
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${userinfo.token}`,
        },
      };
      const response = await axios.delete(`/products/delete/${id}`, config);
      dispatch({ type: productdeletesuccess, payload: response });
    } catch (error) {
      dispatch({
        type: productdeletefail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};

export const createproduct = () => {
  return async (dispatch, getState) => {
    try {
      dispatch({ type: productcreaterequest });
      const {
        userlogin: { userinfo },
      } = getState();
      const config = {
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${userinfo.token}`,
        },
      };
      const { data } = await axios.post("/products/create/", {}, config);
      console.log(data);
      dispatch({ type: productcreatesuccess, payload: data });
    } catch (error) {
      dispatch({
        type: productcreatefail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};

export const updateproduct = (product) => {
  return async (dispatch, getState) => {
    try {
      dispatch({ type: productupdaterequest });
      const {
        userlogin: { userinfo },
      } = getState();
      const config = {
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${userinfo.token}`,
        },
      };
      const { data } = await axios.put(
        `/products/update/${product._id}/`,
        product,
        config
      );
      dispatch({ type: productupdatesuccess, payload: data });
      dispatch({ type: productdetailsuccess, payload: data });
    } catch (error) {
      dispatch({
        type: productupdatefail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};

export const createproductreview = (productid, review) => {
  return async (dispatch, getState) => {
    try {
      dispatch({ type: productcreatereviewrequest });
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
        `/products/${productid}/reviews/`,
        review,
        config
      );
      dispatch({ type: productcreatereviewsuccess, payload: data });
    } catch (error) {
      dispatch({
        type: productcreatereviewfail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};

export const listtopproducts = () => {
  return async (dispatch) => {
    try {
      dispatch({ type: producttoprequest });
      const response = await axios.get(`/products/top/`);
      console.log("response", response);
      dispatch({ type: producttopsuccess, payload: response.data });
    } catch (error) {
      dispatch({
        type: producttopfail,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
};
