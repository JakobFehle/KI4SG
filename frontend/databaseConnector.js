var mysql = require('mysql');

var con = mysql.createConnection({
    host: "localhost",
    database: "kochbar",
    user: "root",
    password: "asdfgh"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected to localhost!");
});