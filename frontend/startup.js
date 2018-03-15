//Initiate Server Instance
//Listing on Port 9009
//Use startServer.bat for instantiation
//Or use "node startup.js" in CMD

var http = require('http');
var db = require('./databaseConnector')

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('FRONTEND');
}).listen(9009);