import React, { Component } from "react";

import axios from "axios";

const formStyle = {
  paddingLeft: "300px",
  paddingTop: "20px"
};
class UserProfile extends Component {
  constructor(props) {
    super(props);

    this.state = {
      name: "",
      email: "",
      location: "",
      isvalid: true
    };
    this.handleNameChange = this.handleNameChange.bind(this);
    this.handleEmailChange = this.handleEmailChange.bind(this);
    this.handleLocationChange = this.handleLocationChange.bind(this);
  }

  handleNameChange(e) {
    this.setState({ name: e.target.value });
  }

  handleEmailChange(e) {
    this.setState({ email: e.target.value });
  }

  handleLocationChange(e) {
    this.setState({ location: e.target.value });
  }

  handleSubmit = event => {
    event.preventDefault();

    var user = {};
    user["name"] = this.state.name;
    user["email"] = this.state.email;
    user["location"] = this.state.location;

    axios
      .post("http://149.165.170.57:4000/api/UserProfiles", user, {
        headers: { crossDomain: true }
      })
      .then(function(res) {
        console.log(res);
        alert("User Registration Succesful!");
      })
      .catch(function(err) {
        alert("User exists with this mail id");
        console.log(err);
      });
    event.target.reset();
  };

  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-md-6" />
          <div className="col-md-4 text-right">
            <a className=".navbar-right" href="/">
              Search
            </a>
          </div>
          <div class="col-md-2 text-right">
            <a className="" href="/details">
              UserProfile
            </a>
          </div>
        </div>

        <h2>Registration</h2>
        <form onSubmit={this.handleSubmit} style={formStyle}>
          <div className="form-group row">
            <label className="col-sm-2">User Name</label>
            <div className="col-sm-4 float-sm-left">
              <input
                type="text"
                required
                className="form-control"
                id="username"
                onChange={this.handleNameChange}
              />
            </div>
          </div>
          <div className="form-group row">
            <label className="col-sm-2">Email</label>
            <div className="col-sm-4 float-sm-left">
              <input
                type="text"
                required
                className="form-control"
                id="useremail"
                onChange={this.handleEmailChange}
              />
            </div>
          </div>
          <div className="form-group row">
            <label className="col-sm-2">Location</label>
            <div className="col-sm-4 float-sm-left">
              <input
                type="text"
                className="form-control"
                id="userlocation"
                onChange={this.handleLocationChange}
              />
            </div>
          </div>
          <div className="form-group row form-btn">
            <div className="col-sm-7">
              <button type="submit" className="btn btn-primary mb-2 btn-color">
                Submit
              </button>
            </div>
          </div>
          <div className="col-sm-5" />
        </form>
      </div>
    );
  }
}

export default UserProfile;
