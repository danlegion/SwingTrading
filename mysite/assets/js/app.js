var React = require('react')

module.exports = React.createClass({
   render: function(){
     console.log(this.props.data)
     var node = this.props.data.map(function(obj){
       return <h2>{obj.id}</h2>
     });

    //  return <h1>Hello {this.props.data.id}</h1>
       return <h1>Hello, world. {node}</h1>
   }
})
