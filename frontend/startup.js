//Initiate Server Instance
//Listing on Port 9009
//Use startServer.bat for instantiation
//Or use "node startup.js" in CMD


var db = require('./databaseConnector')
var express = require('express');
var app = express();

app.get('/', function (req, res) {
  res.send(dboutput);
});

app.listen(9009, function () {
  console.log('Server startet @localhost:9009');
});