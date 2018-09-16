import React, { Component } from "react";

import axios from "axios";

const formStyle = {
  paddingLeft:'300px',
  paddingTop: '20px'
}

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
      <div className="container">
        <form onSubmit={this.handleSubmit} style={formStyle}>
          <div className="form-group row">
            <label className="col-sm-2">
              Email
            </label>
            <div className="col-sm-4 float-sm-left">
              <input
                type="text"
                className="form-control"
                id="useremail"
                onChange={this.handleEmailChange}
              />
            </div>
          </div>

          <div className="form-group row form-btn">
            <div className="col-sm-7">
              <button type="submit" className="btn btn-primary mb-2 btn-color">
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
