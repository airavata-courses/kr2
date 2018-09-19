import React, { Component } from "react";

import axios from "axios";
import "./UserDetails.css";

class UserDetails extends Component {
  constructor() {
    super();
    this.state = {
      email: "",
      userName: undefined,
      location: "",
      isSubmitted: false
    };
    this.handleEmailChange = this.handleEmailChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleDisplayChange = this.handleDisplayChange.bind(this);
  }
  handleEmailChange(e) {
    this.setState({ email: e.target.value });
  }
  handleDisplayChange(bool) {
    this.setState({ isSubmitted: bool });
  }

  handleSubmit = event => {
    event.preventDefault();

    axios
      .get("/api/UserProfiles/fetchByMail/" + this.state.email)
      .then(res => {
        if (res.data) {
          console.log(res.data.email);
          this.setState({ userName: res.data.name });
          this.setState({ location: res.data.location });
          this.setState({ email: res.data.email });
          this.handleDisplayChange(true);
        } else {
          this.setState({ isSubmitted: false });
          this.setState({ userName: "" });
        }
      })
      .catch(err => {
        console.log(err);
        alert("Please enter registered email id");
        this.handleDisplayChange(false);
      });

    event.target.reset();
  };

  render() {
    const { isSubmitted } = this.state;
    return (
      <div>
        {!isSubmitted ? (
          <div className="container">
            <a className="navigationlink" href="/profile">

              User Registration
            </a>
            <a className="navigationlink1" href="/">Search </a>
            <form onSubmit={this.handleSubmit}>
              <div className="form-group row">
                <label className="col-sm-4">
                  Email
                </label>
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

              <div className="form-group row form-btn">
                <div className="col-sm-12">
                  <button type="submit" className="btn btn-primary mb-2 btn-color">
                    Go
                  </button>
                  <p> If you are a new user, please register first</p>
                </div>
                <div className="col-sm-5">
                  {this.state.userName === "" &&
                    alert("Please enter registered email id")}
                </div>
              </div>
            </form>
          </div>
        ) : (
          <div>
            <div>
              <a className="navigationlink" href="/">
                Search
              </a>
              {this.state.userName !== "" && (
                <div className="card">
                  <h1>{this.state.userName}</h1>
                  <p>{this.state.email}</p>
                  <p>{this.state.location}</p>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    );
  }
}

export default UserDetails;
