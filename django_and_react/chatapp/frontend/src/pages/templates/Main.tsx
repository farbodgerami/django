import { useTheme } from "@emotion/react";
import { Box } from "@mui/material";
import React, { ReactNode } from "react";

interface Props {children:ReactNode}
const Main = ({children}:Props) => {
    const theme=useTheme()
  return (
    <Box
      sx={{
        flexGrow: 1,
        mt: `${theme.primaryAppBar.height}px`,
        height: `calc(100vh - ${theme.primaryAppBar.height}px)`,overflow:'hidden'
      }}
    >
        {children}
    </Box>
  );
};

export default Main;
