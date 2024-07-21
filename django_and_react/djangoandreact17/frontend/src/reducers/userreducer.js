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
  userresetprofile,
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
  userupdatereset,
  userupdatesuccess,
} from "../constants/userconstants";

const initialstate = localStorage.getItem("userinfo")
  ? JSON.parse(localStorage.getItem("userinfo"))
  : null;
export const userloginreducers = (
  state = { userinfo: initialstate },
  action
) => {
  switch (action.type) {
    case userloginrequest:
      return { loading: true };
    case userloginsuccess:
      return { loading: false, userinfo: action.payload };
    case userloginfail:
      return { loading: false, error: action.payload };
    case userlogout:
      return {};

    default:
      return state;
  }
};

export const userregisterreducers = (
  state = { userinfo: initialstate },
  action
) => {
  switch (action.type) {
    case userregisterrequest:
      return { loading: true };
    case userregistersuccess:
      return { loading: false, userinfo: action.payload };
    case userregisterfail:
      return { loading: false, error: action.payload };
    case userlogout:
      return {};

    default:
      return state;
  }
};

export const userdetailsreducers = (state = { user: {} }, action) => {
  
  switch (action.type) {
    case userdetailsrequest:
      return { ...state, loading: true };
    case userdetailssuccess:
      return { loading: false, user: action.payload };
    case userdetailsfail:
      return { loading: false, error: action.payload };
    case userdetailsreset:
   
      return { user: {} };

    default:
      return state;
  }
};



export const userlistreducer = (state = { users: [] }, action) => {
  switch (action.type) {
    case userlistrequest:
      return { loading: true };
    case userlistsuccess:
      return { loading: false, success: true, users: action.payload };
    case userlistfail:
      return { loading: false, error: action.payload };
    case userlistreset:
      return { users: [] };

    default:
      return state;
  }
};

export const userdeletereducer = (state = {}, action) => {
  switch (action.type) {
    case userdeleterequest:
      return { loading: true };
    case userdeletesuccess:
      return { loading: false, success: true };
    case userdeletefail:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};

export const userupdatereducer = (state = {user:{}}, action) => {
  switch (action.type) {
    case userupdaterequest:
      return { loading: true };
    case userupdatesuccess:
      return { loading: false, success: true };
    case userupdatefail:
      return { loading: false, error: action.payload };
    case userupdatereset:
        return { loading: false, error: action.payload };

    default:
      return state;
  }
};
// in vase profile

export const userupdatereducers = (state = {}, action) => {
  switch (action.type) {
    case userupdateprofilerequest:
      return { loading: true };
    case userupdateprofilesuccess:
      return { loading: false, success: true, user: action.payload };
    case userupdateprofilefail:
      return { loading: false, error: action.payload };
    case userresetprofile:
      return {};

    default:
      return state;
  }
};