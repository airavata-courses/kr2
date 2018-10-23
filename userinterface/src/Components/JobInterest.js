import React, { Component } from "react";

import axios from "axios";

class JobInterest extends Component {
  constructor() {
    super();
    this.state = {
      email: "",
      jobInterest: [],
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
      .get("http://149.165.170.240:9090/jobInterest/" + this.state.email)
      .then(
        function(res) {
          if (res.data) {
            if (res.data.length === 0)
              alert("No Records of Job Interest Found!!");
            this.handleDisplayChange(true);
            var newArr = this.state.jobInterest.concat(res.data);
            this.setState({ jobInterest: newArr });
            console.log("Array: A " + this.state.jobInterest);
          } else {
            this.setState({ isSubmitted: false });
          }
        }.bind(this)
      )
      .catch(err => {
        console.log(err);
        alert("No Records Found!!");
        this.handleDisplayChange(false);
      });

    event.target.reset();
  };

  render() {
    const { isSubmitted } = this.state;

    var { jobInterest } = this.state;

    return (
      <div>
        {!isSubmitted ? (
          <div className="container">
            <a className="navigationlink" href="/profile">
              Registration
            </a>
            <a className="navigationlink1" href="/">
              Search{" "}
            </a>
            <form onSubmit={this.handleSubmit}>
              <div className="form-group row">
                <label className="col-sm-4">Email</label>
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
                  <button
                    type="submit"
                    className="btn btn-primary mb-2 btn-color"
                  >
                    Go
                  </button>
                  <p> Enter registered email to retrieve job interests</p>
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
                  <p>{this.state.email}</p>
                  <ul>
                    {jobInterest.map(function(name, index) {
                      return <li key={index}>{name}</li>;
                    })}
                  </ul>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    );
  }
}

export default JobInterest;
