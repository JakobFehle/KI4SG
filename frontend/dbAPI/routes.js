var express = require("express"),
    bodyParser = require("body-parser"),
    db = require("./databaseConnector.js");

module.exports = (function () {
    "use strict";

    var api = express.Router();

    api.use(bodyParser.urlencoded());
    api.use(bodyParser.json());


    api.get("/userInformation", function (req, res) {
        var sqlQuery = 'SELECT * FROM newschema.users WHERE UserID = ' + db.escape(req.query.id) + ' AND Date LIKE "' + new Date().toISOString().slice(0, 10).replace('T', ' ') + ' %";';
        db.query(sqlQuery, (err, nutritions) => {
            if (err) {
                console.log(err);
                res.json({
                    "status": "error",
                    "data": err
                });
            }
            var sqlQuery2 = 'SELECT * FROM newschema.referencenuts WHERE Geschlecht = ' + db.escape(req.query.sex) + ' AND newschema.referencenuts.Alter_Obergrenze > ' + db.escape(req.query.age) + ' AND newschema.referencenuts.Alter_Untergrenze <= ' + db.escape(req.query.age) + ' LIMIT 1;'

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
        var sqlQuery1 = 'SELECT * FROM newschema.recipenuts WHERE RezeptID =' + db.escape(req.body.rezeptID) + ';',
            nuts;

        db.query(sqlQuery1, (err, rows) => {
            if (err) console.log(err);
            nuts = rows[0];
            var sqlQuery2 = 'INSERT INTO newschema.users(UserID,RezeptID,Kcal,Eiweis,Kohlenhydrate,Fett,Calcium,Kalium,Eisen,Zink,Magnesium,Ballaststoffe,Linolsaeure,Linolensaeure,Iodid,VitaminA,VitaminC,VitaminE,VitaminB1,VitaminB2,VitaminB6,VitaminB12,Date) VALUES(' +
                db.escape(req.body.userID) + ',' +
                db.escape(nuts.RezeptID) + ',' +
                db.escape(parseFloat(nuts.Kcal) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.Eiweis) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.Kohlenhydrate) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.Fett) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.Calcium) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.Kalium) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.Eisen) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.Zink) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.Magnesium) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.Ballaststoffe) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.Linolsaeure) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.Linolensaeure) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.Iodid) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.VitaminA) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.VitaminC) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.VitaminE) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.VitaminB1) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.VitaminB2) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.VitaminB6) * parseFloat(req.body.propsEaten)) + ',' +
                db.escape(parseFloat(nuts.VitaminB12) * parseFloat(req.body.propsEaten)) + ',"' +
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
        var searchString = req.query.text.toString(),
            searchStringArray = [],
            sqlQuery = 'SELECT * FROM (SELECT * FROM newschema.recipenuts WHERE newschema.recipenuts.RezeptID LIKE ';

        searchString = searchString.toLowerCase();
        searchString = searchString.replace(" von ", " ");
        searchString = searchString.replace(" aus ", " ");
        searchString = searchString.replace(" mit ", " ");
        searchString = searchString.replace(" ohne ", " ");
        searchString = searchString.replace(" oder ", " ");
        searchString = searchString.replace(" und ", " ");
        searchString = searchString.replace(";", "");
        searchString = searchString.replace(":", "");
        searchString = searchString.replace(",", "");
        searchString = searchString.replace(".", "");
        searchString = searchString.replace("\"", "");
        searchString = searchString.replace("'", "");
        searchString = searchString.replace("-", "");
        searchString = searchString.replace("ä", "ae");
        searchString = searchString.replace("ü", "ue");
        searchString = searchString.replace("ö", "oe");
        searchString = searchString.replace("ß", "ss");

        searchStringArray = searchString.split(/\s+/);
        sqlQuery += db.escape("%" + searchStringArray[0] + "%");

        for (var i = 1; i < searchStringArray.length; i++) {
            sqlQuery += ' AND newschema.recipenuts.RezeptID LIKE ' + db.escape('%' + searchStringArray[i] + '%');
        }

        sqlQuery += ' LIMIT 100) t1 inner join (SELECT title, zutaten, furPersonen, Schwierigkeitsgrad, Zubereitungszeit, recipe_href, numstars FROM newschema.kochbar_recipes WHERE newschema.kochbar_recipes.recipe_href LIKE ' +
            db.escape("%" + searchStringArray[0] + "%");

        for (var i = 1; i < searchStringArray.length; i++) {
            sqlQuery += ' AND newschema.kochbar_recipes.recipe_href LIKE ' + db.escape('%' + searchStringArray[i] + '%');
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

    return api;
})();
