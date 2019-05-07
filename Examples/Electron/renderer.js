//Get chart data defined in chart_setup.js
var chart = require("./chart_setup.js").chart;
var electron = require("electron");
var message_count = 0;

//
//Debug message handler
//
electron.ipcRenderer.on("debug-message", function(event, message) {
  console.log("Debug: " + message);
});

//
//"frame" message received from the udp server, forward on to onReceivedNewFrame
//
electron.ipcRenderer.on("frame", function(event, message) {
  //Quick hack to reduce amount of drawing. #todo: Improve performance and run at 60fps
  message_count = message_count + 1;
  if (message_count > 20) {
    message_count = 0;
    //message = {timestamp: getTimeValue(), values: [Math.random() * 100, Math.random() * 100] };   //Debug random testing
    message.timestamp = new Date().getTime();
    onReceivedNewFrame(message);
  }
});

//
// Handle the new frame of telemetry
//
function onReceivedNewFrame(frame) {
  //First append new data to chart data
  var index = 0;
  var num = chart.data.datasets.length;
  while (index < num) {
    chart.data.datasets[index].data.push({
      x: frame.timestamp,
      y: frame.values[index]
    });
    index++;
  }

  // Then update chart datasets keeping the current animation
  chart.update({
    preservation: true
  });
}
