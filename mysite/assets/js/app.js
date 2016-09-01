var React = require('react')
var Recharts = require('recharts')

const {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend} = Recharts;

module.exports = React.createClass({
   render(){
     var json = JSON.parse(this.props.data);
     console.log(json)
      return(
        <LineChart width={600} height={500} data={json}>
          <Line type="monotone" dataKey="Close" stroke="#8884d8" />
          <CartesianGrid stroke="#ccc" strokeDasharray="1 5" />
          <XAxis dataKey="Date" />
          <YAxis />
          <Tooltip/>
        </LineChart>
      );
   }
})
