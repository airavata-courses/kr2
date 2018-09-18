import React, { Component } from "react";
// import {Redirect} from 'react-router-dom';
import axios from "axios";

const formStyle = {
  paddingLeft:'300px',
  paddingTop: '20px'
}

class JobRecommendationForm extends Component {
  constructor(props) {
    super(props);

    this.state = {

      results:"",
    };
  }


  handleRecommendSubmit(e) {

    e.preventDefault();
    axios({
      method: 'get',
      url: 'http://localhost:3050/jobrec',
      config: { headers: {'Content-Type': 'application/json','crossDomain': true }}
    })
        .then(function(res) {
          console.log(res);
        })
        .catch(function(err) {
          console.log(err);
        });
      // console.log(this.state.results);
}



  render() {



    return (
      <div className="container">
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

      </div>
    );
  }
}

export default JobRecommendationForm;
