import React, { Component } from "react";
import UserProfile from "./Components/UserProfile.js";
import UserDetails from "./Components/UserDetails.js";
import { BrowserRouter, Route } from "react-router-dom";
import "./App.css";

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div>
          <Route
            exact={true}
            path="/profile"
            render={() => (
              <div className="App">
                <UserProfile />
              </div>
            )}
          />
          <Route
            exact={true}
            path="/details"
            render={() => (
              <div className="App">
                <UserDetails />
              </div>
            )}
          />
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
