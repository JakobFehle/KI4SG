//ODCB driver needs to be install 
//install via CMD "npm install mysql"

var mysql = require('mysql');


module.exports = (function () {

    var con = mysql.createConnection({
        host: "localhost",
        database: "kochbar",
        user: "root",
        password: "asdfgh"
    });

    con.connect(function (err) {
        if (err) {
            console.log('Error connecting to kochbar@localhost!');
            return;
        };
        console.log("Connected to kochbar@localhost!");
        /*
        con.query('SELECT * FROM kochbar.kochbar_analysis_recipe', (err, rows) => {
            if (err) console.log(err);

            console.log('Data received');
            console.log(rows);
        })
        */
    });

    return con;
})();
