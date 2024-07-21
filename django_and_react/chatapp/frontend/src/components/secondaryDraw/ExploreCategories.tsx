import React, { useEffect } from "react";
import useCruds from "../../hooks/useCruds";
import {
  Box,
  List,
  ListItem,
  ListItemAvatar,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Typography,
} from "@mui/material";
import { useTheme } from "@emotion/react";
import { Link } from "react-router-dom";
import { MEDIAURL } from "../../config";

interface Category {
  id: number;
  name: string;
  description: string;
  icon: string;
}
const ExploreCategories = () => {
  const theme = useTheme();
  const { fetchData, dataCRUD, error, isLoading } = useCruds<Category>(
    [],
    "/server/category/"
  );

  useEffect(() => {
    fetchData();
  }, []);
  console.log('fgggggggggggggggggggggg',dataCRUD)
  return (
    <>
      <Box
        sx={{
          height: "50px",
          display: "flex",
          alignItems: "center",
          px: 2,
          borderBottom: `1px solid ${theme.palette.divider}`,
          position: "sticky",
          top: 0,
          backgroundColor: theme.palette.background.default,
        }}
      >
        Explore
      </Box>
      <List sx={{ py: 0 }}>
        {dataCRUD.map((item,j) => {
          return (
            <ListItem
              disablePadding
              key={item.id}
              sx={{ display: "block" }}
              dense={true}
            >
              <Link
                to={`/explore/${item.name}`}
                style={{ textDecoration: "none", color: "inherit" }}
              >
                <ListItemButton sx={{ minHeight: 48 }}>
                  <ListItemIcon sx={{ minWidth: 0, justifyContent: "center" }}>
                    <ListItemAvatar sx={{ minWidth: "0px" }}>
                    <img
                      // alt="server icon"
                      src={`${MEDIAURL}${item.icon}`}
                   
                      style={{
                        width: "25px",
                        height: "25px",
                        display: "block",
                        margin: "auto",
                      }}
                    />

                    </ListItemAvatar>
                  </ListItemIcon>
                  <ListItemText
                    primary={
                      <Typography
                        varient="body1"
                        textAlign="start"
                        paddingLeft={1}
                      >
                        {item.name}
                      </Typography>
                    }
                  />
                </ListItemButton>
              </Link>
              {/* {item.name} */}
            </ListItem>
          );
        })}
      </List>
    </>
  );
};

export default ExploreCategories;
