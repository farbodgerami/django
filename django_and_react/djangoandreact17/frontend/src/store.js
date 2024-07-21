import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";
import {
  productdetailsreducer,
  productlistreducers,
  productdeletesreducer,
  productcreatereducer,
  productupdatereducer,
  productreviewcreatereducer,producttopratedreducer
} from "./reducers/productresucers";
import { cartreducer } from "./reducers/cartreducers";
import {
  userloginreducers,
  userregisterreducers,
  userdetailsreducers,
  userupdatereducers,
  userlistreducer,
  userdeletereducer,
  userupdatereducer,
} from "./reducers/userreducer";
const reducer = combineReducers({
  productcreate: productcreatereducer,
  productlist: productlistreducers,
  productdetail: productdetailsreducer,
  productdelete: productdeletesreducer,
  productupdate: productupdatereducer,
  cart: cartreducer,
  userlogin: userloginreducers,
  userregister: userregisterreducers,
  userdetails: userdetailsreducers,
  userupdateprofile: userupdatereducers,
  userlist: userlistreducer,
  userdelete: userdeletereducer,
  userupdate: userupdatereducer,
  productcreatereview: productreviewcreatereducer,
  producttoprated:producttopratedreducer,
});

const middleware = [thunk];
const store = createStore(
  reducer,
  composeWithDevTools(applyMiddleware(...middleware))
);
export default store;
