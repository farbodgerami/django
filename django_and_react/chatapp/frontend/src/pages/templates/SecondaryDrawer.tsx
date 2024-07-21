import { useTheme } from "@emotion/react";
import { Box } from "@mui/material";
import { ReactNode } from "react";

interface Props{children:ReactNode}
const SecondaryDrawer = ({children}:Props) => {
  const theme = useTheme();
  return (
    <Box
      sx={{
        minWidth: `${theme.secondaryDraw.width}`,
        height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
        mt: `${theme.primaryAppBar.height}px`,
        // width: theme.primaryDraw.width,
        borderRight: `1px solid ${theme.palette.divider}`,
        display: { xs: "none", sm: "block" },overflow:'auto'
      }}
    >
      {children}
 
    </Box>
  );
};

export default SecondaryDrawer;
