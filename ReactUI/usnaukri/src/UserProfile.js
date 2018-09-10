import React, { Component } from "react";
import "./UserProfile.css";

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

  componentDidMount() {}

  handleSubmit = event => {
    event.preventDefault();
    console.log(this.state.name);
    event.target.reset();
  };
  render() {
    return (
      <div class="container-fluid" className="User">
        <h1> User Profile </h1>

        <form onSubmit={this.handleSubmit}>
          <div class="form-group row">
            <label for="userName" class="col-sm-4">
              Name
            </label>
            <div class="col-sm-3 float-sm-left">
              <input
                type="text"
                class="form-control"
                id="userName"
                onChange={this.handleNameChange}
              />
            </div>
          </div>
          <div class="col-sm-10">
            <button type="submit" class="btn btn-primary mb-2 btn-color">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default UserProfile;
