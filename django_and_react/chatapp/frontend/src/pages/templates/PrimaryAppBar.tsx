import {
  AppBar,
  IconButton,
  Toolbar,
  Typography,
  Box,
  Drawer,
  useMediaQuery,
} from "@mui/material";
import Link from "@mui/material/Link";

import { useTheme } from "@emotion/react";
import MenuIcon from "@mui/icons-material/Menu";
import { useEffect, useState } from "react";
import ExploreCategories from "../../components/secondaryDraw/ExploreCategories";
const PrimaryAppBar = () => {
  const [sideMenu, setSideMenu] = useState<boolean>(false);
  const theme = useTheme();
  const isSmallScreen = useMediaQuery(theme.breakpoints.up("sm"));

  useEffect(() => {
    if (isSmallScreen && sideMenu) {
      setSideMenu(false);
    }
  }, [isSmallScreen]);
  const toggleDrawer = (open: boolean) => {
    setSideMenu(open);
  };
  const list = () => {
    return (
      <Box
        sx={{ paddingTop:'50px', minWidth: 200 }}
        role="presentation"
        onClick={() => toggleDrawer(false)}
        onkeydown={() => toggleDrawer(false)}
      >
<ExploreCategories/>
      </Box>
    );
  };

  return (
    <AppBar
      sx={{
        zIndex: () => theme.zIndex.drawer + 2,
        backgroundColor: theme.palette.background.default,
        borderBottom: `1px solid ${theme.palette.divider}`,
      }}
    >
      <Toolbar
        variant="dense"
        sx={{
          height: theme.primaryAppBar.height,
          minHeight: theme.primaryAppBar.height,
        }}
      >
        <Box sx={{ display: { xs: "block", sm: "none" } }}>
          <IconButton
            onClick={() => toggleDrawer(true)}
            color="inherit"
            aria-label="open drawer"
            edge="start"
            sx={{ mr: 2 }}
          >
            <MenuIcon />
          </IconButton>
        </Box>
        <Drawer
          anchor="left"
          open={sideMenu}
          onClose={() => toggleDrawer(false)}
        >
     {list()}
        </Drawer>
        <Link href="/" underline="none" color="inherit">
          <Typography
            variant="h6"
            noWrap
            component="div"
            sx={{ display: { fontWeight: 700, letterSpacing: "-0.5px" } }}
          >
            DJCHAT
          </Typography>
        </Link>
      </Toolbar>
    </AppBar>
  );
};

export default PrimaryAppBar;
