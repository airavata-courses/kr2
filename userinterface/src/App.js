import React, { Component } from "react";
import UserProfile from "./Components/UserProfile.js";
import "./App.css";

class App extends Component {
  render() {
    return (
      <div className="App">
        <h3> Registration Form</h3>
        <UserProfile />
      </div>
    );
  }
}

export default App;
