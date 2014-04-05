// https://github.com/LearnBoost/socket.io-client
// https://github.com/voodootikigod/node-serialport

// var SerialPort = require("serialport").SerialPort;
// var serialPort = new SerialPort("/dev/tty.usbserial-AH001BS6", /*{ baudrate: 57600 },*/ false); // this is the openImmediately flag [default is true]

var clientio  = require('socket.io-client');         // this is the socket.io client
var socket = clientio.connect('https://192.168.0.100', {port: 8080, secure: true});

// serialPort.open(function () {
//    serialPort.on('data', function(data) {
//        console.log('data received: ' + data);
//    });
//    serialPort.write("ls\n", function(err, results) {
//        console.log('err ' + err);
//        console.log('results ' + results);
//    });
// });

// socket.on('connect', function(){
// 	console.log('connected');

  //   socket.on('dir', function(data){
		// console.log(data);
  //   });

  //   socket.on('disconnect', function(){

  //   });
// });

var room = 'b0';
if (room !== '') {
  console.log('Create or join room', room);
  socket.emit('create or join', room);
}

socket.on('created', function (room){
  console.log('Created room ' + room);
});

socket.on('full', function (room){
  console.log('Room ' + room + ' is full');
});

socket.on('join', function (room){
  console.log('Another peer made a request to join room ' + room);
  console.log('This peer is the initiator of room ' + room + '!');
});

socket.on('joined', function (room){
  console.log('This peer has joined room ' + room);
  isChannelReady = true;
});

socket.on('log', function (array){
  console.log.apply(console, array);
});

////////////////////////////////////////////////

socket.on('message', function (message){
  // console.log('Received message:', message);
  // if (message === 'got user media') {
  //   maybeStart();
  // } else if (message.type === 'offer') {
  //   if (!isInitiator && !isStarted) {
  //     maybeStart();
  //   }
  //   pc.setRemoteDescription(new RTCSessionDescription(message));
  //   doAnswer();
  // } else if (message.type === 'answer' && isStarted) {
  //   pc.setRemoteDescription(new RTCSessionDescription(message));
  // } else if (message.type === 'candidate' && isStarted) {
  //   var candidate = new RTCIceCandidate({sdpMLineIndex:message.label,
  //     candidate:message.candidate});
  //   pc.addIceCandidate(candidate);
  // } else if (message === 'bye' && isStarted) {
  //   handleRemoteHangup();
  // }
  console.log(message);
});