import React, { Component } from "react";

import axios from "axios";

class UserDetails extends Component {
  constructor() {
    super();
    this.state = {
      email: "",
      users: []
    };
    this.handleEmailChange = this.handleEmailChange.bind(this);
  }
  handleEmailChange(e) {
    this.setState({ email: e.target.value });
  }

  componentDidMount() {}

  handleSubmit = event => {
    event.preventDefault();

    var user = {};

    console.log(user);
    axios
      .get("/api/UserProfiles/fetchByMail/" + this.state.email)
      .then(function(res) {
        console.log(res.data.name);
        console.log(res.data.email);
        console.log(res.data.location);
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
            <label for="useremail" class="col-sm-4">
              Email
            </label>
            <div class="col-sm-5 float-sm-left">
              <input
                type="text"
                class="form-control"
                id="useremail"
                onChange={this.handleEmailChange}
              />
            </div>
          </div>

          <div class="form-group row form-btn">
            <div class="col-sm-12">
              <button type="submit" class="btn btn-primary mb-2 btn-color">
                Go
              </button>
            </div>
          </div>
        </form>
      </div>
    );
  }
}

export default UserDetails;
