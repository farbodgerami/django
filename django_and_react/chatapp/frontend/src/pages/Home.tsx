import { Box, CssBaseline } from "@mui/material";
import PrimaryAppBar from "./templates/PrimaryAppBar";
import PrimaryDraw from "./templates/PrimaryDraw";
import SecondaryDrawer from "./templates/SecondaryDrawer";
import Main from "./templates/Main";
import PopularChannels from "../components/PrimaryDraw/PopularChannels";
import ExploreCategories from "../components/secondaryDraw/ExploreCategories";

import ExploreServer from "../components/Main/ExploreServer";

const Home = () => {
  return (
    <Box sx={{ display: "flex"  }}>
      <CssBaseline />
      <PrimaryAppBar />

      <PrimaryDraw>
        <></>
        {/* <PopularChannels open={false}/> */}
      </PrimaryDraw>
      <SecondaryDrawer>
        <ExploreCategories />
      </SecondaryDrawer>
      <Main>
        <ExploreServer />
      </Main>
    </Box>
  );
};

export default Home;
