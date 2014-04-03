// https://github.com/LearnBoost/socket.io-client
// https://github.com/voodootikigod/node-serialport

var SerialPort = require("serialport").SerialPort;
var serialPort = new SerialPort("/dev/tty-usbserial1", /*{ baudrate: 57600 },*/ false); // this is the openImmediately flag [default is true]
var socket = require('socket.io-client')('https://10.129.26.35:8000');

serialPort.open(function () {
    serialPort.on('data', function(data) {
        console.log('data received: ' + data);
    });

    serialPort.write("ls\n", function(err, results) {
        console.log('err ' + err);
        console.log('results ' + results);
    });
});

socket.on('connect', function(){
    socket.on('dir', function(data){

    });

    socket.on('disconnect', function(){

    });
});
