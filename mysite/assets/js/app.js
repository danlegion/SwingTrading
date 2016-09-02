var React = require('react')
var Recharts = require('recharts')
const {LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend} = Recharts;

const ReactHighcharts = require('react-highcharts');

var config = {
  xAxis: {
    // categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  },
  series: [{
    // data: [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 295.6, 454.4]

  }]
};

module.exports = React.createClass({
  getInitialState: function() {
      return {index: 5, all_data:{}, visible_data:{}};
  },
  componentWillMount(){
    var json = JSON.parse(this.props.data);
    this.setState({all_data: json, visible_data: json})
  },
  componentDidMount() {
    let chart = this.refs.chart.getChart();
    const xx = this.state.visible_data
    var categories = []
    Object.keys(xx).forEach(function(key, keyIndex) {
      // console.log("index:",keyIndex,"key:",key,"value:",xx[key].Date);
      categories.push(xx[key].Date)
    });

    chart.xAxis[0].setCategories(categories, true, true);

    console.log(this.state.index);
    for (var i = 0; i <= this.state.index; i++) {
      chart.series[0].addPoint({x: i, y: xx[i].Close});
    }
    this.setState({index: this.state.index+1})
  },
  render(){
     var self = this
    //  var json = this.state.visible_data;

    //  console.log(json)
      // return(
      //   <div>
      //   <LineChart width={600} height={300} data={json}>
      //     <Line type="monotone" dataKey="Close" stroke="#8884d8" />
      //     <CartesianGrid stroke="#ccc" strokeDasharray="1 5" />
      //     <XAxis dataKey="Date" />
      //     <YAxis />
      //     <Tooltip/>
      //   </LineChart>
      //   <input type="button" onClick={self.handleThatEvent} value="Click Me!" />
      //   </div>
      // );
      return(
        <div>
        <ReactHighcharts config={config} ref="chart"></ReactHighcharts>
        <input type="button" onClick={self.handleThatEvent} value="Click Me!" />
        </div>
      );
    },
    shouldComponentUpdate: function(nextProps, nextState) {
        return nextState.index === this.props.index;
    },
    handleThatEvent: function(e){

      let chart = this.refs.chart.getChart();
      this.setState({index: this.state.index+1})
      // this.setState({visible_data: this.state.all_data.slice(0,this.state.index)})
      // console.log(this.state.index)

      const xx = this.state.visible_data
      chart.series[0].addPoint({x: this.state.index, y: xx[this.state.index].Close});
      // console.log(xx,this.state.index,xx[this.state.index].Close);
    }
})
