import { useTheme } from "@emotion/react";
import { Box, Drawer, easing, useMediaQuery, styled } from "@mui/material";
import React, { useEffect, useState,ReactNode } from "react";
import DrawToggle from "../../components/PrimaryDraw/DrawToggle";
import axios from "axios";
import useAxioswithinterceptor from "../../helpers/jwtinterceptors";
import PopularChannels from "../../components/PrimaryDraw/PopularChannels";
 
interface Props{children:ReactNode}
// interface ChildProps{open:boolean}
// type ChildElement=React.ReactElement<ChildProps>

const PrimaryDraw:React.FC<Props> = ({children}:Props) => {
  const below600 = useMediaQuery("(max-width:599px)");
  const [open, setOpen] = useState(!below600);
  const theme = useTheme();

  const jwtAxios=useAxioswithinterceptor()
  // axios
  jwtAxios
  .get("http://localhost:8000/api/server/select/?category=cat1")
  .then((res) => console.log(res.data))
  .catch((e) => console.log(e));
  
  useEffect(() => {
    setOpen(!below600);
  }, [below600]);
  const handleDrawerOpen = () => {
    setOpen(true);
  };
  const handleDrawerClose = () => {
    setOpen(false);
  };
  return (
    <Drawer
      PaperProps={{
        sx: {
          mt: `${theme.primaryAppBar.height}px`,
          height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
          minWidth: open ? theme.primaryDraw.width : '4rem',
          position:'relative'
        },
      }}
      open={open}
      variant={below600 ? "temporary" : "permanent"}
    >
      <Box>
        <Box
          sx={{
            position: "absolute",
            top: 0,
            right: 0,
            p: 0,
            width: open ? "auto" : "100%",
          }}
        >
          <DrawToggle
            open={open}
            handleDrawerClose={handleDrawerClose}
            handleDrawerOpen={handleDrawerOpen}
          />
 
 
        </Box>
        <PopularChannels open={open}/>
     {/* {children} */}
      </Box>
    </Drawer>
  );
};

export default PrimaryDraw;
