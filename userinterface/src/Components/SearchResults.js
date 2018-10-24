import React, { Component } from "react";
import DisplayResults from "./DisplayResults.js";

const searchlink = {
  fontSize: "20px",
  paddingLeft: "800px"
};
class SearchResults extends Component {
  render() {
    let searchResults;
    if (this.props.location.state.results.length > 0) {
      searchResults = this.props.location.state.results.map(search => {
        return <DisplayResults key={search.id} search={search} />;
      });
    }
    return (
      <div className="App">
        <a href="/" style={searchlink}>
          Search Again
        </a>

        <h2>Displaying {this.props.location.state.results.length} results</h2>
        <br />
        <div className="container">
          <table border="1">
            <tr>
              <th>Company</th>
              <th>Job Title</th>
              <th>Company url</th>
              <th> Job Type</th>
              <th>Location </th>
              <th>How to apply</th>
            </tr>
            {searchResults}
          </table>
        </div>
      </div>
    );
  }
}

export default SearchResults;
