import React, { Component } from "react";
import UserProfile from "./Components/UserProfile.js";
import UserDetails from "./Components/UserDetails.js";
import SearchForm from "./Components/SearchForm.js";
import SearchResults from "./Components/SearchResults.js";
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
            <Route exact ={true} path = "/" render = {() => (
            <div className="App">
              <SearchForm />
            </div>
          )}/>

          <Route exact path="/searchresults" component={SearchResults}/>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
