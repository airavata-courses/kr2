import React, { Component } from "react";
import { Redirect } from "react-router-dom";
import axios from "axios";

const formStyle = {
  paddingLeft: "300px",
  paddingTop: "20px"
};
const searchlink = {
  paddingLeft: "650px",
  fontSize: "15px"
};
const searchlink1 = {
  paddingLeft: "80px",
  fontSize: "15px"
};

const radioStyle = {
  width: "70%"
};
class SearchForm extends Component {
  constructor(props) {
    super(props);

    this.state = {
      job: {},

      results: []
    };
    // this.handleDescChange = this.handleDescChange.bind(this);
  }

  handleSearchSubmit(e) {
    e.preventDefault();
    //console.log(this.state.desc);
    var bodyFormData = new FormData();
    var jobTypeValue;

    if (
      this.refs.email.value === "" ||
      this.refs.desc.value === "" ||
      (document.getElementById("radio1").checked === false &&
        document.getElementById("radio2").checked === false)
    ) {
      alert("Fields required");
    } else {
      if (document.getElementById("radio1").checked) {
        jobTypeValue = "true";
      } else {
        jobTypeValue = "false";
      }
      this.setState(
        {
          job: {
            desc: this.refs.desc.value,
            city: this.refs.city.value,
            title: this.refs.title.value,
            jobType: jobTypeValue,
            email: this.refs.email.value
          }
        },
        function() {
          bodyFormData.set("desc", this.state.job["desc"]);
          bodyFormData.set("city", this.state.job["city"]);
          bodyFormData.set("title", this.state.job["title"]);
          bodyFormData.set("jobType", this.state.job["jobType"]);
          bodyFormData.set("email", this.state.job["email"]);
          // console.log(this.state.job);
          // console.log(bodyFormData.values());
          axios({
            method: "post",
            url: "http://149.165.170.151:5000/job",
            data: bodyFormData,
            config: {
              headers: {
                "Content-Type": "multipart/form-data",
                crossDomain: true
              }
            }
          })
            .then(response => {
              let data = {
                results:
                  response.data["result"].length === 0
                    ? { 1: 0 }
                    : response.data["result"]
              };

              // console.log(response.data['result']);
              this.setState(data);
              // console.log(this.state.results);
            })
            .catch(function(err) {
              //handle error
              console.log(err);
            });
        }
      );
    }
  }

  render() {
    return (
      <div className="container">
        <a href="/details" style={searchlink}>
          Profile
        </a>
        <a href="/jobinterest" style={searchlink1}>
          JobInterest
        </a>

        <h2> US Naukri </h2>
        <form onSubmit={this.handleSearchSubmit.bind(this)} style={formStyle}>
          <div className="form-group row">
            <label className="col-sm-2">Job Description</label>
            <div className="col-sm-4 float-sm-left">
              <input type="text" required className="form-control" ref="desc" />
            </div>
          </div>
          <div className="form-group row">
            <label className="col-sm-2">Location</label>
            <div className="col-sm-4 float-sm-left">
              <input type="text" className="form-control" ref="city" />
            </div>
          </div>
          <div className="form-group row">
            <label className="col-sm-2">Job Title</label>
            <div className="col-sm-4 float-sm-left">
              <input type="text" className="form-control" ref="title" />
            </div>
          </div>
          <div className="form-group row">
            <label className="col-sm-2">Email</label>
            <div className="col-sm-4 float-sm-left">
              <input
                type="text"
                required
                className="form-control"
                ref="email"
              />
            </div>
          </div>
          <div className="form-group row">
            <label className="col-sm-2">Limit results only to Full-Time</label>
            <div className="col-sm-1 float-sm-left">
              <input
                id="radio1"
                type="radio"
                style={radioStyle}
                value="true"
                className="form-control"
                name="jobType"
              />
              YES
            </div>
            <div className="col-sm-1 float-sm-left">
              <input
                type="radio"
                id="radio2"
                style={radioStyle}
                value="false"
                className="form-control"
                name="jobType"
              />
              NO
            </div>
          </div>

          <div className="form-group row form-btn">
            <div className="col-sm-7">
              <button type="submit" className="btn btn-primary mb-2 btn-color">
                Search
              </button>
            </div>
          </div>
        </form>
        <br />
        {this.state.results.length > 0 && (
          <Redirect
            to={{
              pathname: "/searchresults",
              state: { results: this.state.results }
            }}
          />
        )}
        {this.state.results[1] === 0 && <p>No search results found</p>}
      </div>
    );
  }
}

export default SearchForm;
