var express = require("express"),
    bodyParser = require("body-parser"),
    db = require("./databaseConnector.js");

module.exports = (function () {
    "use strict";

    var api = express.Router();

    api.use(bodyParser.urlencoded());
    api.use(bodyParser.json());


    api.get("/userInformation", function (req, res) {
        var sqlQuery = 'SELECT * FROM newschema.users WHERE UserID = "' + req.query.id + '";';
        db.query(sqlQuery, (err, rows) => {
            if (err) {
                console.log(err);
                res.json({
                    "status": "error",
                    "data": err
                })
            }

            res.json({
                "status": "success",
                "data": rows
            });

        });
    });

    api.put("/userInformation", function (req, res) {
        var sqlQuery1 = 'SELECT * FROM newschema.recipenuts WHERE RezeptID ="' + req.body.rezeptID + '";',
            nuts;

        db.query(sqlQuery1, (err, rows) => {
            if (err) console.log(err)
            nuts = rows[0];

            var sqlQuery2 = 'INSERT INTO newschema.users(UserID,RezeptID,Kcal,Eiweis,Kohlenhydrate,Fett,Calcium,Kalium,Eisen,Zink,Magnesium,Ballaststoffe,Linolsaeure,Linolensaeure,Iodid,VitaminA,VitaminC,VitaminE,VitaminB1,VitaminB2,VitaminB6,VitaminB12,Date) VALUES("' +
                req.body.userID + '","' +
                nuts.RezeptID + '","' +
                nuts.Kcal + '","' +
                nuts.Eiweis + '","' +
                nuts.Kohlenhydrate + '","' +
                nuts.Fett + '","' +
                nuts.Calcium + '","' +
                nuts.Kalium + '","' +
                nuts.Eisen + '","' +
                nuts.Zink + '","' +
                nuts.Magnesium + '","' +
                nuts.Ballaststoffe + '","' +
                nuts.Linolsaeure + '","' +
                nuts.Linolensaeure + '","' +
                nuts.Iodid + '","' +
                nuts.VitaminA + '","' +
                nuts.VitaminC + '","' +
                nuts.VitaminE + '","' +
                nuts.VitaminB1 + '","' +
                nuts.VitaminB2 + '","' +
                nuts.VitaminB6 + '","' +
                nuts.VitaminB12 + '","' +
                req.body.date + '");';

            db.query(sqlQuery2, (err, rows) => {
                if (err) {
                    res.json({
                        "status": "error",
                        "sql": sqlQuery2,
                        "data": err
                    });
                }
                res.json({
                    "data": "success"
                });
            });
        });
    });

    api.get("/getRecipeInformation", function (req, res) {
        //var sqlQuery = 'SELECT * FROM newschema.kochbar_recipes'
        res.json({
            "status": "success"
        });
    });

    api.get("/getNutrInformation", function (req, res) {
        var sqlQuery = 'SELECT * FROM newschema.recipenuts WHERE RezeptID ="' + req.query.id + '";';
        db.query(sqlQuery, (err, rows) => {
            if (err) {
                res.json({
                    "status": "error",
                    "data": err
                });
            }
            res.json({
                "status": "success",
                "data": rows
            });
        });
    });

    return api;
})();

//"/rezept/501707/Gefuellte-Zucchini-und-Paprika.html"
