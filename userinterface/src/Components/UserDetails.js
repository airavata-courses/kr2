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
        } else {
          this.setState({ isSubmitted: false });
          this.setState({ userName: "" });
        }
      })
      .catch(err => {
        //alert("Inavlid email id, please provide registered email id");
        console.log(err);
        this.setState({ isSubmitted: false });
      });

    //Display the details
    if (this.state.email !== "") {
      this.handleDisplayChange(true);
    } else {
      alert("Please enter registered email id");
    }
    event.target.reset();
  };

  render() {
    const { isSubmitted } = this.state;
    return (
      <div>
        {!isSubmitted ? (
          <div class="container-fluid" className="ApplicationForm">
            <a className="navigationlink" href="/profile">
              User Registration
            </a>
            <form onSubmit={this.handleSubmit}>
              <div class="form-group row">
                <label for="useremail" class="col-sm-4">
                  Email
                </label>
                <div class="col-sm-5 float-sm-left">
                  <input
                    type="text"
                    required
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
                  <p> If you are a new user, please register first</p>
                </div>

                <div class="col-sm-5">
                  {this.state.userName === "" && (
                    <div class="alert alert-danger" role="alert">
                      User not present
                    </div>
                  )}
                </div>
              </div>
            </form>
          </div>
        ) : (
          <div>
            <div>
              {this.state.userName !== "" && (
                <div class="card">
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
