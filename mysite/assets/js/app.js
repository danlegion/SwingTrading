var React = require('react')
var Recharts = require('recharts')

const {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend} = Recharts;

module.exports = React.createClass({
   render(){
      return(
        <LineChart width={400} height={400} data={this.props.data}>
          <Line type="monotone" dataKey="value" stroke="#8884d8" />
          <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip/>
        </LineChart>
      );
   }
})
