import { Box, CssBaseline } from "@mui/material";
import PrimaryAppBar from "./templates/PrimaryAppBar";
import PrimaryDraw from "./templates/PrimaryDraw";
import SecondaryDrawer from "./templates/SecondaryDrawer";
import Main from "./templates/Main";
import PopularChannels from "../components/PrimaryDraw/PopularChannels";
import ExploreCategories from "../components/secondaryDraw/ExploreCategories";
import ExploreServer from "../components/Main/ExploreServer";

const Explore = () => {

  return (
    <Box sx={{ display: "flex"  }}>
      <CssBaseline />
      <PrimaryAppBar />
 
      <PrimaryDraw>
        <div>vase khali naboodane arize</div>
       {/* <PopularChannels open={false}/> */}
      </PrimaryDraw>
      <SecondaryDrawer>
      <ExploreCategories/>

      </SecondaryDrawer>
      <Main>
        <ExploreServer />
      </Main>
    </Box>
  );
};

export default Explore;
