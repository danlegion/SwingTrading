var React = require('react')
var dom = require('react-dom')
var App = require('./app')
var Recharts = require('recharts')

var Content = React.createClass({
  loadContentFromServer: function(){
       $.ajax({
           url: this.props.url,
           datatype: 'json',
           cache: false,
           success: function(data) {
               this.setState({data: data});
           }.bind(this)
       })
   },

   getInitialState: function() {
       return {data: []};
   },

   componentDidMount: function() {
       this.loadContentFromServer();
   },

   render: function() {
        if (this.state.data.length > 0) {
          console.log('DATA!')
            console.log(this.state.data)
            return (<App data={[this.state.data]}/>);
        }
        return (
            <div>
                <h1>Hello React!{this.state.data}</h1>
            </div>
        );
    }
});

dom.render(<Content url='/polls/a' />, document.getElementById('react-app'))
// dom.render(<App data={[{name:'a', value:20},{name:'b',value:30},{name:'b',value:25}]} />, document.getElementById('react-app'))

// React.render(<App/>, document.getElementById('react-app'))

// const {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend} = Recharts;
// const data = [
//       {name: 'Page A', uv: 4000, pv: 2400, amt: 2400},
//       {name: 'Page B', uv: 3000, pv: 1398, amt: 2210},
//       {name: 'Page C', uv: 2000, pv: 9800, amt: 2290},
//       {name: 'Page D', uv: 2780, pv: 3908, amt: 2000},
//       {name: 'Page E', uv: 1890, pv: 4800, amt: 2181},
//       {name: 'Page F', uv: 2390, pv: 3800, amt: 2500},
//       {name: 'Page G', uv: 3490, pv: 4300, amt: 2100},
// ];
// const SimpleLineChart = React.createClass({
// 	render () {
//   	return (
//     	<LineChart width={600} height={300} data={data}
//             margin={{top: 5, right: 30, left: 20, bottom: 5}}>
//        <XAxis dataKey="name"/>
//        <YAxis/>
//        <CartesianGrid strokeDasharray="3 3"/>
//        <Tooltip/>
//        <Legend />
//        <Line type="monotone" dataKey="pv" stroke="#8884d8" activeDot={{r: 8}}/>
//        <Line type="monotone" dataKey="uv" stroke="#82ca9d" />
//       </LineChart>
//     );
//   }
// })
//
// dom.render(
//   <SimpleLineChart />,
//   document.getElementById('react-app')
// );
