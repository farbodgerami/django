// import {  useSelector } from "react-redux";
import { BrowserRouter as Router, Route,
  // Redirect 
} from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import { Container } from "react-bootstrap";
import Homescreen from "./screens/Homescreen";
import Productscreen from "./screens/Productscreen";
import Cartscreen from "./screens/Cartscreen";
import Loginscreen from "./screens/Loginscreen";
import Registerscreen from "./screens/registerscreen";
import Profilescreen from './screens/profilescreen'
import Userlistscreen from './screens/userlistscreen'
import Usereditscreen from './screens/Usereditscreen'
import Productlistscreen from './screens/Productlistscreen'
import Producteditscreen from './screens/Producteditscreen'

function App() {
  // const userlogin=useSelector(state=>state.userlogin)
  // const { userinfo}=userlogin
  return (
    <Router>
      <Header />
      <Container>
        <main className="py-3">
          <Container>
        
          <Route component={Cartscreen} path="/cart/:id?"  />  
          <Route component={Loginscreen} path="/login"  />  
          <Route component={Registerscreen} exact path="/register"  /> 
          {/* {userinfo?
          <Route component={Homescreen} path="/" exact />:
          <Route path='/' exact><Redirect to='/login'/></Route>
        } */}
        <Route component={Homescreen} path="/" exact />
          <Route component={Productscreen} path="/product/:id"  /> 
          <Route component={Profilescreen} path="/profile"  /> 
          <Route component={Userlistscreen} path="/admin/userlist"  /> 
          <Route component={Usereditscreen} path="/admin/user/:id/edit"  /> 
          <Route component={Productlistscreen} path="/admin/productlist"  /> 
          <Route component={Producteditscreen} path="/admin/product/:id/edit"  /> 
       
          </Container>
        </main>
      </Container>
      <Footer />
    </Router>
  );
}

export default App;
