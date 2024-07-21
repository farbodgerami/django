import {
  Avatar,
  Link,
  List,
  ListItem,
  ListItemAvatar,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Typography,
} from "@mui/material";
import { Box } from "@mui/system";
import useCruds from "../../hooks/useCruds";
import { useEffect } from "react";
import { MEDIAURL } from "../../config";

interface Props {
  open: boolean;
}
interface Server {
  id: number;
  name: string;
  description: string;
  icon: string;
  category: string;
}
const PopularChannels = ({ open }: Props) => {
  const { fetchData, dataCRUD, error, isLoading } = useCruds<Server>(
    [],
    "/server/select/"
  );
  useEffect(() => {
    fetchData();
    console.log("inside", dataCRUD);
  }, []);
  // TODO vase gereftane ettelaat darim:
  useEffect(() => {
    // console.log(dataCRUD);
  }, [dataCRUD]);
  // console.log(dataCRUD)
  return (
    <>
      <Box
        sx={{
          height: 50,
          p: 2,
          display: "flex",
          alignItems: "center",
          flex: "1 1 100%",
          background: "blue",
        }}
      >
        <Typography sx={{ display: open ? "block" : "none" }}>
          Popular
        </Typography>
      </Box>
      <List>
        {dataCRUD.map((item) => (
          <ListItem
            key={item.id}
            disablePadding
            sx={{ display: "block" }}
            dense={true}
          >
            <Link
              to={`/server/${item.id}`}
              style={{ textDecoration: "none", color: "inherit" }}
            >
              <ListItemButton sx={{ minHeight: 0 }}>
                <ListItemIcon sx={{ minWidth: 0, justifyContent: "center" }}>
                  <ListItemAvatar sx={{ minWidth: "50px" }}>
                    <Avatar alt="server icon" src={`${MEDIAURL}${item.icon}`} />
                  </ListItemAvatar>
                </ListItemIcon>
                <ListItemText
                  primary={
                    <Typography
                      variant="body2"
                      sx={{
                        fontWeight: 700,
                        lineHeight: 1.2,
                        textOverflow: "ellipsis",
                        overflow: "hidden",
                        whiteSpace: "nowrap",
                      }}
                    >
                      {item.name}
                    </Typography>
                  }
                  secondary={
                    <Typography
                      variant="body2"
                      sx={{
                        fontWeight: 500,
                        lineHeight: 1.2,
                        color: "textSecondary",
                      }}
                    >
                      {item.category}
                    </Typography>
                  }
                  sx={{ opacity: open ? 1 : 0 }}
                  primaryTypographyProps={{
                    sx: {
                      textOverflow: "ellipsis",
                      overflow: "hidden",
                      whitespace: "nowrap",
                    },
                  }}
                />
              </ListItemButton>
            </Link>
          </ListItem>
        ))}
      </List>
    </>
  );
};

export default PopularChannels;
