// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

console.log("Loaded renderer.js");

var ctx = document.getElementById('myChart').getContext('2d');
var chartColors = {
	red:    'rgb(255,  99, 132)',
	orange: 'rgb(255, 159,  64)',
	yellow: 'rgb(255, 205,  86)',
	green:  'rgb( 75, 192, 192)',
	blue:   'rgb( 54, 162, 235)',
	purple: 'rgb(153, 102, 255)',
	grey:   'rgb(201, 203, 207)'
};
var color = Chart.helpers.color;

Chart.defaults.global.elements.line.fill = false;
Chart.defaults.global.elements.line.radius = 0.0;
Chart.defaults.global.elements.line.cubicInterpolationMode = 'monotone';
Chart.defaults.global.elements.point.radius = 0.0;

var chart = new Chart(ctx, {
  type: 'line',
  data: {
    datasets: [{
      label: 'Speed',
      yAxisID: "ySpeed",
			backgroundColor: color(chartColors.orange).alpha(0.5).rgbString(),
			borderColor: chartColors.orange,
			data: []
		}, {
      label: 'RPM',
      yAxisID: "yRPM",
			backgroundColor: color(chartColors.blue).alpha(0.5).rgbString(),
			borderColor: chartColors.blue,
			data: []
    }, {
      label: 'Throttle',
      yAxisID: "yThrottle",
			backgroundColor: color(chartColors.green).alpha(0.5).rgbString(),
			borderColor: chartColors.green,
			data: []
    }, {
      label: 'Brake',
      yAxisID: "yBrake",
			backgroundColor: color(chartColors.red).alpha(0.5).rgbString(),
			borderColor: chartColors.red,
			data: []
    }, {
      label: 'Steer',
      yAxisID: "ySteer",
			backgroundColor: color(chartColors.purple).alpha(0.5).rgbString(),
			borderColor: chartColors.purple,
			data: []
    }
  ]
  },
  options: {
    layout: {
          padding: {
              left: 10,
              right: 10,
              top: 10,
              bottom: 10
          }
    },
    scales: {

      xAxes: [{
        type: 'realtime',
        realtime: {
          pause: false,
          frameRate: 30
        }
      }],

      yAxes: [{
          id: "ySpeed" ,
          display: true,
          position: 'left',
          type: "linear",
          ticks: {
            min: -10.0,
            max: 40.0,
          },
          scaleLabel: {
              display: true,
              labelString: 'speed (m/s)',
              beginAtZero: true,
          },        
        },{
            id: "yRPM",
            display: true, 
            position:"right",
            type: "linear",
            ticks: {
              min: 0.0,
              max: 16000.0,
            },
            scaleLabel: {
              display: true,
              labelString: 'rpm',
              beginAtZero: true,
            },
            gridLines: {
                display: false
            },        
        },{
            id: "yThrottle",
            display: true, 
            position:"right",
            type: "linear",
            ticks: {
              min: 0.0,
              max: 1.0,
            },
            scaleLabel: {
              display: true,
              labelString: 'throttle',
              beginAtZero: true,
            },
            gridLines: {
                display: false
            }, 
        },{
            id: "yBrake",
            display: true, 
            position:"right",
            type: "linear",
            ticks: {
              min: 0.0,
              max: 1.0,
            },
            scaleLabel: {
              display: true,
              labelString: 'brake',
              beginAtZero: true,
            },
            gridLines: {
                display: false
            }
        },{
            id: "ySteer",
            display: true, 
            position:"right",
            type: "linear",
            ticks: {
              min: -100.0,
              max: 100.0,
            },
            scaleLabel: {
              display: true,
              labelString: 'steer',
              beginAtZero: true,
            },
            gridLines: {
                display: false
            }, 
        },
      ]
    }
  }
});

// your event listener code - assuming the event object has the timestamp and value properties
function onReceive(event) {

  // append the new data to the existing chart data
  var index = 0;
  var num = chart.data.datasets.length;
  while(index < num) {
    chart.data.datasets[index].data.push({
        x: event.timestamp,
        y: event.values[index]
    });
    index++;
  }

  // update chart datasets keeping the current animation
  chart.update({
      preservation: true
  });
}

function getTimeValue() {
    var dateBuffer = new Date();
    var Time = dateBuffer.getTime();
    return Time;
  }

//Debug message handler
require('electron').ipcRenderer.on('debug-message', function(event, message) {
  console.log("Debug: " + message);  
});

count = 0;
require('electron').ipcRenderer.on('frame', function(event, message) {

    //Quick hack to reduce amount of drawing. #todo: Improve performance and run at 60fps
    count = count + 1;
    if (count > 20)
    {      
      count = 0;   
      //message = {timestamp: getTimeValue(), values: [Math.random() * 100, Math.random() * 100] };   //Debug random testing
      message.timestamp = new Date().getTime();
      onReceive(message);
    }

  });