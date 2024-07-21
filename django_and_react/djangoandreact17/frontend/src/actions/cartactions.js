import axios from "axios";
import { cartadditem, cartremoveitem } from "../constants/cartconstants";
export const addtocart = (id, qty) => {
  return async (dispatch, getstate) => {
    const { data } = await axios.get(`/products/${id}`);
    dispatch({
      type: cartadditem,
      payload: {
        product: data._id,
        name: data.name,
        image: data.image,
        price: data.price,
        countinstocks: data.countinstocks,
        qty,
      },
    });
    localStorage.setItem(
      "cartitems",
      JSON.stringify(getstate().cart.cartitems)
    );
  };
};

export const removefromdart = (id) => {
  return (dispatch, getstate) => {
    dispatch({ type: cartremoveitem, payload: id });
    localStorage.setItem('cartitems',JSON.stringify(getstate().cart.cartitems))
  };
};
