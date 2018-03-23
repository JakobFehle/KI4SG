var express = require("express"),
    bodyParser = require("body-parser"),
    db = require("./databaseConnector.js");

module.exports = (function () {
    "use strict";

    var api = express.Router();

    api.use(bodyParser.urlencoded());
    api.use(bodyParser.json());


    api.get("/getUserInformation", function (req, res) {
        db.query('SELECT * FROM kochbar.kochbar_analysis_recipe', (err, rows) => {
            if (err) console.log(err);

            res.json({
                "status": "success",
                "data": rows[0]
            });

        });
    });

    api.put("/updateUserInformation", function (req, res) {
        res.json({
            "status": "success"
        });
    });

    api.get("/getRecipeInformation", function (req, res) {
        res.json({
            "status": "success"
        });
    });

    return api;
})();
