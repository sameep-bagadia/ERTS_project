// https://github.com/LearnBoost/socket.io-client
// https://github.com/voodootikigod/node-serialport

var SerialPort = require("serialport").SerialPort;
var serialPort = new SerialPort("/dev/tty.usbserial-AH001BS6", /*{ baudrate: 57600 },*/ false); // this is the openImmediately flag [default is true]

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

socket.on('connect', function(){
	console.log('connected');
	
    socket.on('dir', function(data){
		console.log(data);
    });

    socket.on('disconnect', function(){

    });
});
