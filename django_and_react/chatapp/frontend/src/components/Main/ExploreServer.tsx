import React, { useEffect } from "react";
import { useParams } from "react-router-dom";
import useCruds from "../../hooks/useCruds";
import {
  Avatar,
  Box,
  Card,
  CardContent,
  CardMedia,
  Grid,
  Link,
  List,
  ListItem,
  ListItemAvatar,
  ListItemIcon,
  ListItemText,
  Typography,
} from "@mui/material";
import Container from "@mui/material";
import { MEDIAURL } from "../../config";

interface Server {
  id: number;
  name: string;
  description: string;
  icon: string;
  category: string;
  banner:string
}

const ExploreServer = () => {
  const { categoryName } = useParams();
  const url = categoryName
    ? `/server/select/?category=${categoryName}`
    : "/server/select";
  console.log(categoryName);
  const { fetchData, dataCRUD, error, isLoading } = useCruds<Server>([], url);
  console.log(dataCRUD);
  useEffect(() => {
    fetchData();
  }, [categoryName]);
  return (
    <>
      <Box maxWidth="lg">
        <Box sx={{ pt: 6 }}>
          <Typography
            variant="h3"
            noWrap
            component="h1"
            sx={{
              display: {
                sm: "block",
                fontWeight: 700,
                fontSize: "48px",
                letterSpacing: "-2px ",
              },
              textAlign: { xs: "center", sm: "left" },
            }}
          >
            {categoryName ? categoryName : "Popular Channels"}
          </Typography>
        </Box>
        <Box>
          <Typography
            variant="h6"
            noWrap
            component="h2"
            color="textSecondary"
            sx={{
              display: {
                sm: "block",
                fontWeight: 700,
                fontSize: "48px",
                letterSpacing: "-2px ",
              },
              textAlign: { xs: "center", sm: "left" },
            }}
          >
            {categoryName
              ? `Channels talking about ${categoryName}`
              : "Check out some of our popular channels"}
          </Typography>
        </Box>
        <Typography
          varient="h6"
          sx={{ pt: 6, pb: 1, fontWeight: 700, letterSpacing: "-1px" }}
        >
          Recommanded Channelds
        </Typography>
        <Grid
          container
          // spacing={{ xs: 0, sm: 2 }}
        >
          {dataCRUD.map((item) => {
            return (
              <Grid item key={item.id} xs={12} sm={6} md={6} lg={3}>
                <Card
                  sx={{
                    height: "100%",
                    display: "flex",
                    flexDirection: "column",
                    boxShadow: "none",
                    backgroundImage: "none",
                  }}
                >
                  <Link
                    to={`/server/${item.id}`}
                    style={{ textDecoration: "none", color: "inherit" }}
                  >
                    <CardMedia
                      component="img"
                      image={item.banner?MEDIAURL+item.banner:"https://source.unsplash.com/random/"}
                      alt="random image"
                      sx={{ display: { sx: "none", sm: "black" } }}
                    />
                    <CardContent
                      sx={{
                        flexGrow: 1,
                        p: 0,
                        "&last-child": { paddingButton: 0 },
                      }}
                    >
                      <List>
                        <ListItem disablePadding>
                          <ListItemIcon sx={{ minWidth: 0 }}>
                            <ListItemAvatar sx={{ minWidth: "50px" }}>
                              <Avatar
                                alt="server icon"
                                src={`${MEDIAURL}${item.icon}`}
                              />
                            </ListItemAvatar>
                          </ListItemIcon>
                          <ListItemText
                            primary={
                              <Typography
                                variant="body2"
                                textAlign="start"
                                sx={{
                                  // lineHeight: 1.2,
                                  textOverflow: "ellipsis",
                                  overflow: "hidden",
                                  whiteSpace: "nowrap",
                                  fontWeight: 700,
                                }}
                              >
                                {item.name}
                              </Typography>
                            }
                            secondary={
                              <Typography
                                variant="body2"
                              
                              >
                                {item.category}
                              </Typography>
                            }
                        
                          />
                        </ListItem>
                      </List>
                    </CardContent>
                  </Link>
                </Card>
              </Grid>
            );
          })}
        </Grid>
      </Box>
    </>
  );
};

export default ExploreServer;
