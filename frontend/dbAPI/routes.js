var express = require("express"),
    bodyParser = require("body-parser"),
    db = require("./databaseConnector.js");

module.exports = (function () {
    "use strict";

    var api = express.Router();

    api.use(bodyParser.urlencoded());
    api.use(bodyParser.json());


    api.get("/userInformation", function (req, res) {
        var sqlQuery = 'SELECT * FROM newschema.users WHERE UserID = "' + req.query.id + '" AND Date = "' + new Date().toISOString().slice(0, 19).replace('T', ' ') + '";';
        db.query(sqlQuery, (err, nutritions) => {
            if (err) {
                console.log(err);
                res.json({
                    "status": "error",
                    "data": err
                });
            }
            var sqlQuery2 = 'SELECT * FROM newschema.referencenuts WHERE Geschlecht = "' + req.query.sex + '" AND newschema.referencenuts.Alter_Obergrenze > ' + req.query.age + ' AND newschema.referencenuts.Alter_Untergrenze <= ' + req.query.age + ' LIMIT 1;'

            db.query(sqlQuery2, (err, nutritionsRef) => {
                if (err) {
                    console.log(err);
                    res.json({
                        "status": "error",
                        "data": err
                    });
                }
                res.json({
                    "status": "success",
                    "data": {
                        nutrs: nutritions,
                        nutrRef: nutritionsRef
                    }
                });

            });
        });
    });
    api.put("/userInformation", function (req, res) {
        var sqlQuery1 = 'SELECT * FROM newschema.recipenuts WHERE RezeptID ="' + req.body.rezeptID + '";',
            nuts;

        db.query(sqlQuery1, (err, rows) => {
            if (err) console.log("yes" + err);
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
                new Date().toISOString().slice(0, 19).replace('T', ' ') + '");';

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
        var searchString = req.query.text,
            searchStringArray = [],
            sqlQuery = 'SELECT * FROM (SELECT * FROM newschema.recipenuts WHERE newschema.recipenuts.RezeptID LIKE "%';

        searchString.toLowerCase();
        searchString.replace("von", "");
        searchString.replace("aus", "");
        searchString.replace("mit", "");
        searchString.replace("ohne", "");
        searchString.replace("oder", "");
        searchString.replace("und", "");
        searchString.replace(";", "");
        searchString.replace(":", "");
        searchString.replace(",", "");
        searchString.replace(".", "");
        searchString.replace("\"", "");
        searchString.replace("'", "");
        searchString.replace("-", "");
        searchString.replace("ä", "ae");
        searchString.replace("ü", "ue");
        searchString.replace("ö", "oe");
        searchString.replace("ß", "ss");
        searchString.replace("drop", "");
        searchString.replace("alter", "");
        searchString.replace("*", "");
        searchString.replace("select", "");
        searchString.replace("table", "");
        searchString.replace("where", "");

        searchStringArray = searchString.split(/\s+/);
        sqlQuery += searchStringArray[0] + '%"';

        for (var i = 1; i < searchStringArray.length; i++) {
            sqlQuery += ' AND newschema.recipenuts.RezeptID LIKE "%' + searchStringArray[i] + '%"';
        }

        sqlQuery += ' LIMIT 100) t1 inner join (SELECT title, zutaten, Schwierigkeitsgrad, Zubereitungszeit, recipe_href, numstars FROM newschema.kochbar_recipes WHERE newschema.kochbar_recipes.recipe_href LIKE "%' + searchStringArray[0] + '%"';

        for (var i = 1; i < searchStringArray.length; i++) {
            sqlQuery += ' AND newschema.kochbar_recipes.recipe_href LIKE "%' + searchStringArray[i] + '%"';
        }

        sqlQuery += ') t2 on t1.RezeptID = t2.recipe_href COLLATE utf8_unicode_ci;';

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

    /*
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
    */
    return api;
})();

//"/rezept/501707/Gefuellte-Zucchini-und-Paprika.html"
