import React, { Component } from "react";
import UserProfile from "./Components/UserProfile.js";
import UserDetails from "./Components/UserDetails.js";
import SearchForm from "./Components/SearchForm.js";
import SearchResults from "./Components/SearchResults.js";
import JobInterest from "./Components/JobInterest.js";
import { BrowserRouter, Route } from "react-router-dom";
import axios from "axios";
import "./App.css";

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      NodeServer: "",
      FlaskServer: "",
      JavaServer: ""
    };
  }
  componentDidMount() {
    axios
      .get("http://149.165.156.241:5000/service_query", {
        headers: { crossDomain: true }
      })
      .then(
        function(res) {
          if (res.data) {
            this.setState({
              NodeServer: res.data["node"]
            });

            this.setState({
              FlaskServer: res.data["flask"]
            });

            this.setState({
              JavaServer: res.data["java"]
            });

            console.log("printing server node " + this.state.NodeServer);
            console.log("printing server flask " + this.state.FlaskServer);
            console.log("printing server java " + this.state.JavaServer);
          } else {
            this.setState({ isSubmitted: false });
          }
        }.bind(this)
      )
      .catch(err => {
        console.log(err);
      });
  }
  render() {
    return (
      <BrowserRouter>
        <div>
          <Route
            exact={true}
            path="/profile"
            render={() => (
              <div className="App">
                <UserProfile server={this.state.NodeServer} />
              </div>
            )}
          />
          <Route
            exact={true}
            path="/details"
            render={() => (
              <div className="App">
                <UserDetails server={this.state.NodeServer} />
              </div>
            )}
          />
          <Route
            exact={true}
            path="/"
            render={() => (
              <div className="App">
                <SearchForm server={this.state.FlaskServer} />
              </div>
            )}
          />
          <Route
            exact={true}
            path="/jobinterest"
            render={() => (
              <div className="App">
                <JobInterest server={this.state.JavaServer} />
              </div>
            )}
          />

          <Route exact path="/searchresults" component={SearchResults} />
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
