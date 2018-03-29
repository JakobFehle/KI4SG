var NutrFinder = NutrFinder || {},
    MMEventTarget = MMEventTarget || {};

NutrFinder.model = function (backendAdress) {
    "use strict";

    var that = new MMEventTarget(),
        userID,
        userAge,
        userSex;

    function setUser(user) {
        userID = user.id;
        userAge = user.age;
        userSex = user.sex;
    }

    function getUserInformation() {
        $.ajax({
            method: "GET",
            url: backendAdress + "userInformation",
            data: {
                "id": userID,
                "age": userAge,
                "sex": userSex
            },
            dataType: "json",
            contentType: "application/json"
        }).done(function (res) {
            res.data.nutrRef = res.data.nutrRef[0];
            if (res.data.nutrs.length == 0) {
                res.data.nutrs = {};
                res.data.nutrs.Kcal = 0;
                res.data.nutrs.Ballaststoffe = 0;
                res.data.nutrs.Calcium = 0;
                res.data.nutrs.Eisen = 0;
                res.data.nutrs.Eiweis = 0;
                res.data.nutrs.Fett = 0;
                res.data.nutrs.Iodid = 0;
                res.data.nutrs.Kalium = 0;
                res.data.nutrs.Kohlenhydrate = 0;
                res.data.nutrs.Linolsaeure = 0;
                res.data.nutrs.Linolensaeure = 0;
                res.data.nutrs.Magnesium = 0;
                res.data.nutrs.VitaminA = 0;
                res.data.nutrs.VitaminB1 = 0;
                res.data.nutrs.VitaminB2 = 0;
                res.data.nutrs.VitaminB6 = 0;
                res.data.nutrs.VitaminB12 = 0;
                res.data.nutrs.VitaminC = 0;
                res.data.nutrs.VitaminE = 0;
                res.data.nutrs.Zink = 0;
            } else if (res.data.nutrs.length == 1) {
                res.data.nutrs = res.data.nutrs[0];
            } else {
                var placeholder = {};
                placeholder.Kcal = 0;
                placeholder.Ballaststoffe = 0;
                placeholder.Calcium = 0;
                placeholder.Eisen = 0;
                placeholder.Eiweis = 0;
                placeholder.Fett = 0;
                placeholder.Iodid = 0;
                placeholder.Kalium = 0;
                placeholder.Kohlenhydrate = 0;
                placeholder.Linolsaeure = 0;
                placeholder.Linolensaeure = 0;
                placeholder.Magnesium = 0;
                placeholder.VitaminA = 0;
                placeholder.VitaminB1 = 0;
                placeholder.VitaminB2 = 0;
                placeholder.VitaminB6 = 0;
                placeholder.VitaminB12 = 0;
                placeholder.VitaminC = 0;
                placeholder.VitaminE = 0;
                placeholder.Zink = 0;
                for (var i = 0; i < res.data.nutrs.length; i++) {
                    placeholder.Kcal += parseFloat(res.data.nutrs[i].Kcal);
                    placeholder.Ballaststoffe += parseFloat(res.data.nutrs[i].Ballaststoffe) / 1000; //transform to g
                    placeholder.Calcium += parseFloat(res.data.nutrs[i].Calcium);
                    placeholder.Eisen += parseFloat(res.data.nutrs[i].Eisen) / 1000; // transform to mg
                    placeholder.Eiweis += parseFloat(res.data.nutrs[i].Eiweis) / 1000; // to g
                    placeholder.Fett += parseFloat(res.data.nutrs[i].Fett) / 1000; // to g
                    placeholder.Iodid += parseFloat(res.data.nutrs[i].Iodid);
                    placeholder.Kalium += parseFloat(res.data.nutrs[i].Kalium);
                    placeholder.Kohlenhydrate += parseFloat(res.data.nutrs[i].Kohlenhydrate) / 1000; // to g
                    placeholder.Linolsaeure += parseFloat(res.data.nutrs[i].Linolsaeure);
                    placeholder.Linolensaeure += parseFloat(res.data.nutrs[i].Linolensaeure);
                    placeholder.Magnesium += parseFloat(res.data.nutrs[i].Magnesium);
                    placeholder.VitaminA += parseFloat(res.data.nutrs[i].VitaminA) / 1000; // to mg
                    placeholder.VitaminB1 += parseFloat(res.data.nutrs[i].VitaminB1) / 1000; // to mg
                    placeholder.VitaminB2 += parseFloat(res.data.nutrs[i].VitaminB2) / 1000; // to mg
                    placeholder.VitaminB6 += parseFloat(res.data.nutrs[i].VitaminB6) / 1000; // to mg
                    placeholder.VitaminB12 += parseFloat(res.data.nutrs[i].VitaminB12);
                    placeholder.VitaminC += parseFloat(res.data.nutrs[i].VitaminC) / 1000; // to mg
                    placeholder.VitaminE += parseFloat(res.data.nutrs[i].VitaminE) / 1000; // to mg
                    placeholder.Zink += parseFloat(res.data.nutrs[i].Zink) / 1000; // to mg
                }
                res.data.nutrs = placeholder;
            }
            for (var index in res.data.nutrs) {
                res.data.nutrs[index] = Math.round(res.data.nutrs[index] * 100) / 100;
            }


            that.dispatchEvent({
                type: "userDataRecieved",
                data: res
            });
        }).fail(function (code, err) {
            console.log(err);
        });
    }

    function updateUserInformation(rezeptID, proportionsEaten) {
        $.ajax({
            method: "PUT",
            url: backendAdress + "userInformation",
            data: JSON.stringify({
                "userID": userID,
                "rezeptID": rezeptID,
                "propsEaten": proportionsEaten
            }),
            dataType: "json",
            contentType: "application/json",
        }).done(function (res) {
            that.dispatchEvent({
                type: "userDataUpdated",
                data: res
            });
        }).fail(function (code, err) {
            console.log(err);
        });
    }

    function getRecipeBySearch(searchInput) {
        $.ajax({
            method: "GET",
            url: backendAdress + "getRecipeInformation",
            data: {
                "text": searchInput
            },
            dataType: "json",
            contentType: "application/json",
        }).done(function (res) {
            that.dispatchEvent({
                type: "recipeSearchFinished",
                data: res
            });
        }).fail(function (code, err) {
            console.log(err);
        });
    }



    function init() {
        that.getRecipeBySearch = getRecipeBySearch;
        that.getUserInformation = getUserInformation;
        that.updateUserInformation = updateUserInformation;
        that.setUser = setUser;
        return that;
    }

    return init();
};
