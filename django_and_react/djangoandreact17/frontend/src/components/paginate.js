import React from "react";
import { Pagination } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

const Paginate = ({ pages, page, keyword = "", isadmin = false }) => {
 
  // if(keyword){keyword=keyword.split()}
  let kw = "";

  if (keyword) {
    // const a=keyword.split('&')

    // const akeyword=a[0].split('=')
    // kw=akeyword[1]

    kw = keyword.split("&")[0].split("=")[1];
  }
  const arr=[...Array(10).keys()]
  // console.log(arr)
  return (
    pages > 1 && (
      <Pagination>
        {/* returns a number to an array */}
        {[...Array(pages).keys()].map((x) => (
          <LinkContainer
            key={x + 1}
            to={
              isadmin
                ? `/admin/productlist/?keyword=${kw}&page=${x + 1}`
                : `/?keyword=${kw}&page=${x + 1}`
            }
          >
            <Pagination.Item active={x + 1 === page}>{x + 1}</Pagination.Item>
          </LinkContainer>
        ))}
      </Pagination>
    )
  );
};

export default Paginate;
