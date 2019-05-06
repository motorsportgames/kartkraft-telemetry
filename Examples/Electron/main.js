var flatbuffers = require('./js/flatbuffers.js').flatbuffers;
var KartKraft = require('./js/Frame_generated.js').KartKraft;
const { app, BrowserWindow } = require("electron");
var PORT = 5000;
var HOST = "127.0.0.1";
var dgram = require("dgram");
var server = dgram.createSocket("udp4");
const {ipcMain} = require('electron')

console.log("After server created");

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let window;

function createWindow() {

  console.log("Creating window");

  //app.dock.hide()



  // Create the browser window.
  window = new BrowserWindow({
    width: 600,
    height: 300,
    transparent: true,
    frame: false,
    transparent: true,
    backgroundColor: '#80000000',
    webPreferences: {
      nodeIntegration: true
    }
  });

  window.setAlwaysOnTop(true, 'floating')
  window.setVisibleOnAllWorkspaces(true)
  window.setFullScreenable(false)
  //app.dock.show()

  console.log("Loading HTML");

  // and load the index.html of the app.
  window.loadFile("index.html");
  window.webContents.on('did-finish-load', () => {

    //Bind socket after window is loaded
    server.bind(PORT, HOST);
  })

  //mainWindow.
  // Open the DevTools.
  // mainWindow.webContents.openDevTools()

  // Emitted when the window is closed.
  window.on("closed", function() {
    // Dereference the window object, usually you would store windows
    // in an array if your app supports multi windows, this is the time
    // when you should delete the corresponding element.
    window = null;
  });
}

// Called when server socket is ready to receive data
server.on("listening", function() {
  var address = server.address();
  var msg = "UDP Server listening on " + address.address + ":" + address.port;

  console.log(msg);
  window.webContents.send('debug-message', msg)
});

// Called when a packet is received
server.on("message", function(message, remote) {

 // var msg = "Received some telemetry!";
  //console.log(msg);

  var buf = new flatbuffers.ByteBuffer(message);  //new
  var frame = KartKraft.Frame.getRootAsFrame(buf);
  if (frame) {
    //Get motion/data/session objects from the frame
    motion = frame.motion();
    dash = frame.dash();
    session = frame.session();

    if (dash) {
      window.webContents.send('frame', {timestamp: frame.timestamp(), values: [dash.speed(), dash.rpm(), dash.throttle(), dash.brake(), dash.steer()]});
    }
  }
});

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on("ready", createWindow);

// Quit when all windows are closed.
app.on("window-all-closed", function() {

  server.close();
  // On macOS it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== "darwin") app.quit();
});

app.on("activate", function() {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (window === null) createWindow();
});

