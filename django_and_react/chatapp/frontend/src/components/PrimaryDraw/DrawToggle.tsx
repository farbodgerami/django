import { ChevronLeft, ChevronRight } from "@mui/icons-material";
import { Box, IconButton } from "@mui/material";
import React from "react";

type Props = {
  open: boolean;
  handleDrawerClose: () => void;
  handleDrawerOpen: () => void;
};
// const DrawToggle:React.FC<Props> = (props:Props) => {
const DrawToggle = ({
  open,
  handleDrawerClose,
  handleDrawerOpen,
}:Props) => {
  return (
    <Box
      sx={{
        height: "50px",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <IconButton onClick={open ? handleDrawerClose : handleDrawerOpen}>
        {open ? <ChevronLeft /> : <ChevronRight />}
      </IconButton>
    </Box>
  );
};

export default DrawToggle;
