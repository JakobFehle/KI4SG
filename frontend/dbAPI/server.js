//Initiate Server Instance
//Listing on Port 9009
//Use startServer.bat for instantiation
//Or use "node server.js" in CMD

const standardPort = 9009;

var express = require('express'),
    api = require("./routes.js"),
    app = express(),
    port = process.env.PORT || standardPort;


app.get('/', function (req, res) {
    res.send('FRONTEND!');
    next();
});

app.use("/api", api);
app.listen(port, function () {
    console.log('Server startet @localhost:9009');
});
