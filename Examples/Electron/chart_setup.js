//
// Chart configuration. Variables, colours, style etc.
//

var ctx = document.getElementById("myChart").getContext("2d");
var chartColors = {
  red: "rgb(255,  99, 132)",
  orange: "rgb(255, 159,  64)",
  yellow: "rgb(255, 205,  86)",
  green: "rgb( 75, 192, 192)",
  blue: "rgb( 54, 162, 235)",
  purple: "rgb(153, 102, 255)",
  grey: "rgb(201, 203, 207)"
};
var color = Chart.helpers.color;

Chart.defaults.global.elements.line.fill = false;
Chart.defaults.global.elements.line.radius = 0.0;
Chart.defaults.global.elements.line.borderWidth = 1;
Chart.defaults.global.elements.line.cubicInterpolationMode = "monotone";
Chart.defaults.global.elements.point.radius = 0.0;

var chart = new Chart(ctx, {
  type: "line",
  data: {
    datasets: [
      {
        label: "Speed",
        yAxisID: "ySpeed",
        backgroundColor: color(chartColors.orange)
          .alpha(0.5)
          .rgbString(),
        borderColor: chartColors.orange,
        data: []
      },
      {
        label: "RPM",
        yAxisID: "yRPM",
        backgroundColor: color(chartColors.blue)
          .alpha(0.5)
          .rgbString(),
        borderColor: chartColors.blue,
        data: []
      },
      {
        label: "Throttle",
        yAxisID: "yThrottle",
        backgroundColor: color(chartColors.green)
          .alpha(0.5)
          .rgbString(),
        borderColor: chartColors.green,
        data: []
      },
      {
        label: "Brake",
        yAxisID: "yBrake",
        backgroundColor: color(chartColors.red)
          .alpha(0.5)
          .rgbString(),
        borderColor: chartColors.red,
        data: []
      },
      {
        label: "Steer",
        yAxisID: "ySteer",
        backgroundColor: color(chartColors.purple)
          .alpha(0.5)
          .rgbString(),
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
      },
      animation: {
        duration: 0 // general animation time
      },
      hover: {
        animationDuration: 0 // duration of animations when hovering an item
      },
      responsiveAnimationDuration: 0, // animation duration after a resize
      plugins: {
        streaming: {
          frameRate: 5 // chart is drawn 30 times every second
        }
      }
    },
    scales: {
      xAxes: [
        {
          type: "realtime",
          realtime: {
            pause: false,
            frameRate: 5
          }
        }
      ],

      yAxes: [
        {
          id: "ySpeed",
          display: true,
          position: "left",
          type: "linear",
          ticks: {
            min: -10.0,
            max: 40.0
          },
          scaleLabel: {
            display: true,
            labelString: "speed (m/s)",
            beginAtZero: true
          }
        },
        {
          id: "yRPM",
          display: true,
          position: "right",
          type: "linear",
          ticks: {
            min: 0.0,
            max: 16000.0
          },
          scaleLabel: {
            display: true,
            labelString: "rpm",
            beginAtZero: true
          },
          gridLines: {
            display: false
          }
        },
        {
          id: "yThrottle",
          display: true,
          position: "right",
          type: "linear",
          ticks: {
            min: 0.0,
            max: 1.0
          },
          scaleLabel: {
            display: true,
            labelString: "throttle",
            beginAtZero: true
          },
          gridLines: {
            display: false
          }
        },
        {
          id: "yBrake",
          display: true,
          position: "right",
          type: "linear",
          ticks: {
            min: 0.0,
            max: 1.0
          },
          scaleLabel: {
            display: true,
            labelString: "brake",
            beginAtZero: true
          },
          gridLines: {
            display: false
          }
        },
        {
          id: "ySteer",
          display: true,
          position: "right",
          type: "linear",
          ticks: {
            min: -100.0,
            max: 100.0
          },
          scaleLabel: {
            display: true,
            labelString: "steer",
            beginAtZero: true
          },
          gridLines: {
            display: false
          }
        }
      ]
    }
  }
});

exports.chart = chart;
