import React, { Component } from "react";
// import {Redirect} from 'react-router-dom';
import axios from "axios";

const formStyle = {
  paddingLeft:'300px',
  paddingTop: '20px'
}
const searchlink = {
  paddingLeft:'800px',
  fontSize: '20px',
}
class JobRecommendationForm extends Component {
  constructor(props) {
    super(props);

    this.state = {

      results:[],
    };
  }


  handleRecommendSubmit(e) {

    e.preventDefault();
    axios({
      method: 'get',
      url: 'http://localhost:3050/jobrec/',
      config: { headers: {'Content-Type': 'application/json','crossDomain': true }}
    })
        // .then(function(res) {
        //   console.log(res.data);
        //
        // })
        .then(response => {
          let data ={
            results: response.data['message'].length===0 ?{1:0}:response.data['message'],
          };
          this.setState(data);
          console.log(this.state.results);
        })
        .catch(function(err) {
          console.log(err);
        });
      // console.log(this.state.results);
}



  render() {



    return (
      <div className="container">
      <a href="/" style ={searchlink}>Search</a>
       <h2> Job Recommendation </h2>
        <form onSubmit={this.handleRecommendSubmit.bind(this)} style ={formStyle}>

          <div className="form-group row form-btn">
            <div className="col-sm-7">
              <button type="submit" className="btn btn-primary mb-2 btn-color">
                Recommend
              </button>
            </div>
          </div>
        </form>
        <br/>
        {this.state.results}
      </div>
    );
  }
}

export default JobRecommendationForm;
