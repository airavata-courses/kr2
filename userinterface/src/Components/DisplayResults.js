import React, { Component } from "react";

class DisplayResults extends Component {
constructor(){
  super();
  this.state ={
    id: 0,
  }
}
  render() {
    function stripHTML(item){
      return item.replace(/<(.|\n)*?>/g, '');
    }
    // function id_index(){
    //   var old_id = this.state.id + 1
    //   this.setState({
    //     id:old_id,
    //   })
    //   return this.state.id
    // }

    return (
      // <li className="App">
      //
      //     <strong>{this.props.search.company}</strong>: {this.props.search.company_url}
      //     <br/>
      //
      // </li>
           <tr>
           <td>{this.props.search.company}</td>
           <td>{this.props.search.title}</td>

           <td>{this.props.search.company_url}</td>
           <td>{this.props.search.type}</td>
           <td>{this.props.search.location}</td>
           <td>{stripHTML(this.props.search.how_to_apply)}</td>
           </tr>




     );

  }
}
export default DisplayResults;
