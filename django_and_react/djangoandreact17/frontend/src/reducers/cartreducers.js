import { cartadditem,cartremoveitem } from "../constants/cartconstants";
const initialstate=localStorage.getItem('cartitems') ? JSON.parse(localStorage.getItem('cartitems')):[]

export const cartreducer = (state = { cartitems: initialstate }, action) => {
  switch (action.type) {
    case cartadditem:
      const item = action.payload;
      const existitem = state.cartitems.find((x) => x.product === item.product);
      if (existitem) {
        return {
          ...state,
          cartitems: state.cartitems.map((x) =>x.product === existitem.product ? item : x),
        };
      } else {
        return { ...state, cartitems: [...state.cartitems, item] };
      }
      case cartremoveitem:
        return {...state,cartitems:state.cartitems.filter(x=>x.product!==action.payload)}
     

    default:
      return state;
  }
};
