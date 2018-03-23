//ODCB driver needs to be install 
//install via CMD "npm install mysql"

var mysql = require('mysql');
var express = require('express');
var app = express();



app.listen(9009, function () {
  console.log('Server startet @localhost:9009');
});

var con = mysql.createConnection({
    host: "localhost",
    database: "newschema",
    user: "root",
    password: "asdfgh"
});

con.connect(function(err) {
  if (err)  {
    console.log('Error connecting to kochbar@localhost!');
      return;
      
      
  };
  console.log("Connected to kochbar@localhost!");
    con.query('SELECT * FROM newschema.recipenuts LIMIT 1' , (err,rows) =>
             { if(err) throw err;
              
              console.log('Data received');
              var dboutput = rows;
              
              console.log(rows);
              app.get('/', function (req, res) {
                    res.send(rows);
});
        
        
    })
});