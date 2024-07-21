import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Carousel, CarouselItem, Image } from "react-bootstrap";
import { listtopproducts } from "../actions/productactions";
import { Link } from "react-router-dom";
const Productcarousel = () => {
  const dispatch = useDispatch();
  const producttoprated = useSelector((state) => state.producttoprated);
  const { error, loading, products } = producttoprated;
 
  useEffect(() => {
      dispatch(listtopproducts())
      
    }, [dispatch]);
    
     

 
  return loading ? (
    <h1>loading...</h1>
  ) : error ? (
    <h1>{error}</h1>
  ) : (
    <Carousel pause="hover" className="bg-dark">
      {products&& products.map((product) => (
        //   <div></div>
        <CarouselItem key={product._id}>
          <Link to={`/product/${product._id}`}>
            <Image src={product.image} alt={product.name} fluid />
            <Carousel.Caption className="carousel.caption">
              <h1>
                {product.name}(${product.price})
              </h1>
            </Carousel.Caption>
          </Link>
        </CarouselItem>
      ))}
    </Carousel>
  );
};

export default Productcarousel;
