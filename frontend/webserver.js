var express = require('express'),
    app = express(),
    http = require('http'),
    httpServer = http.Server(app);

app.use(express.static(__dirname + '/public/'));

app.get('/', function (req, res) {
    res.sendfile('public/index.htm');
});
app.listen(3000);
