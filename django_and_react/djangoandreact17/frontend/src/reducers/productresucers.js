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
  productcreatereset,
  productcreatesuccess,
  productupdatefail,
  productupdaterequest,
  productupdatereset,
  productupdatesuccess,
  productcreatereviewfail,
  productcreatereviewrequest,
  productcreatereviewreset,
  productcreatereviewsuccess,
  producttopfail,
  producttoprequest,
  producttopsuccess,
} from "../constants/productconstants";
export const productlistreducers = (state = { products: [] }, action) => {
  switch (action.type) {
    case productlistrequest:
      return { loading: true, products: [] };
    case productlistsuccess:
      return {
        loading: false,
        products: action.payload.products,
        page: action.payload.page,
        pages: action.payload.pages,
      };
    case productlistfail:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};

export const productdetailsreducer = (state = { product: {} }, action) => {
  switch (action.type) {
    case productdetailrequest:
 
      return { loading: true, ...state };
    case productdetailsuccess:
    
      return { loading: false, product: action.payload };
    case productdetailfail:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};

export const productdeletesreducer = (state = {}, action) => {
  switch (action.type) {
    case productdeleterequest:
      return { loading: true };
    case productdeletesuccess:
      return { loading: false, success: true };
    case productdeletefail:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};

export const productcreatereducer = (state = {}, action) => {
  switch (action.type) {
    case productcreaterequest:
   
      return { loading: true };
    case productcreatesuccess:
    
      return { loading: false, success: true, product: action.payload };
    case productcreatefail:
      return { loading: false, error: action.payload };
    case productcreatereset:
      return {};

    default:
      return state;
  }
};

export const productupdatereducer = (state = { product: {} }, action) => {
  switch (action.type) {
    case productupdaterequest:
      return { loading: true };
    case productupdatesuccess:
      return { loading: false, success: true, product: action.payload };
    case productupdatefail:
      return { loading: false, error: action.payload };
    case productupdatereset:
      return { product: {} };

    default:
      return state;
  }
};

export const productreviewcreatereducer = (state = {}, action) => {
  switch (action.type) {
    case productcreatereviewrequest:
      return { loading: true };
    case productcreatereviewsuccess:
      return { loading: false, success: true };
    case productcreatereviewfail:
      return { loading: false, error: action.payload };
    case productcreatereviewreset:
      return {};

    default:
      return state;
  }
};


 



export const producttopratedreducer = (state = {producs:[]}, action) => {
  switch (action.type) {
    case producttoprequest:
      return { loading: true,products:[] };
    case producttopsuccess:
      return { loading: false, products: action.payload };
    case producttopfail:
      return { loading: false, error: action.payload };
 
    default:
      return state;
  }
};