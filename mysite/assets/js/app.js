var React = require('react')
var Recharts = require('recharts')

const {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend} = Recharts;

module.exports = React.createClass({
   render(){
     var json = JSON.parse(this.props.data);
     console.log(json)
      return(
        <LineChart width={400} height={400} data={json}>
          <Line type="monotone" dataKey="value" stroke="#8884d8" />
          <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip/>
        </LineChart>
      );
   }
})
