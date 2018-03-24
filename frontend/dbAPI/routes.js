var express = require("express"),
    bodyParser = require("body-parser"),
    db = require("./databaseConnector.js");

module.exports = (function () {
    "use strict";

    var api = express.Router();

    api.use(bodyParser.urlencoded());
    api.use(bodyParser.json());


    api.get("/getUserInformation", function (req, res) {
        var sqlQuery = 'SELECT * FROM newschema.users;';
        console.log(sqlQuery);
        db.query(sqlQuery, (err, rows) => {
            if (err) console.log(err);

            res.json({
                "status": "success",
                "data": rows
            });

        });
    });

    api.put("/updateUserInformation", function (req, res) {
        res.json({
            "status": "success"
        });
        /*
        INSERT INTO newschema.users(UserID, RezeptID,Kcal,Eiweis,Kohlenhydrate,Fett,Calcium,Kalium,Eisen,Zink,Magnesium,Ballaststoffe,Linolsaeure,Linolensaeure,Iodid,VitaminA,VitaminC,VitaminE,VitaminB1,VitaminB2,VitaminB6,VitaminB12) 
        VALUES ('1','DavidsLeckerTomatenSupper','1200','5','4','9','9','1','2','22','12','2','12','21','2','21','21','21','21','21','21','2004-05-23T14:25:10');
        */
    });

    api.get("/getRecipeInformation", function (req, res) {
        res.json({
            "status": "success"
        });
    });

    api.get("/getNutrInformation", function (req, res) {
        res.json({
            "status": "success"
        });
    });

    return api;
})();
