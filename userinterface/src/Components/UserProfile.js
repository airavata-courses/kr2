import React, { Component } from "react";

import axios from "axios";

class UserProfile extends Component {
  constructor(props) {
    super(props);

    this.state = {
      name: ""
    };
    this.handleNameChange = this.handleNameChange.bind(this);
  }

  handleNameChange(e) {
    this.setState({ name: e.target.value });
  }

  handleSubmit = event => {
    event.preventDefault();
    console.log(this.state.name);

    var user = {};
    user["name"] = this.state.name;
    axios
      .post("/api/UserProfiles", user)
      .then(function(res) {
        console.log(res);
      })
      .catch(function(err) {
        console.log(err);
      });
    event.target.reset();
  };

  render() {
    return (
      <div class="container-fluid" className="ApplicationForm">
        <form onSubmit={this.handleSubmit}>
          <div class="form-group row">
            <label for="username" class="col-sm-4">
              User Name
            </label>
            <div class="col-sm-5 float-sm-left">
              <input
                type="text"
                class="form-control"
                id="username"
                onChange={this.handleNameChange}
              />
            </div>
          </div>
          <div class="form-group row">
            <label for="username" class="col-sm-4">
              Email
            </label>
            <div class="col-sm-5 float-sm-left">
              <input
                type="text"
                class="form-control"
                id="username"
                onChange={this.handleNameChange}
              />
            </div>
          </div>
          <div class="form-group row">
            <label for="username" class="col-sm-4">
              Location
            </label>
            <div class="col-sm-5 float-sm-left">
              <input
                type="text"
                class="form-control"
                id="username"
                onChange={this.handleNameChange}
              />
            </div>
          </div>
          <div class="form-group row form-btn">
            <div class="col-sm-12">
              <button type="submit" class="btn btn-primary mb-2 btn-color">
                Submit
              </button>
            </div>
          </div>
        </form>
      </div>
    );
  }
}

export default UserProfile;
