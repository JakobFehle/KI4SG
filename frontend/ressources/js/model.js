var NutrFinder = NutrFinder || {},
    MMEventTarget = MMEventTarget || {};

NutrFinder.model = function (backendAdress) {
    "use strict";

    var that = new MMEventTarget();

    function getUserInformation(userID) {
        $.ajax({
            method: "GET",
            url: backendAdress + "userInformation",
            data: {
                "id": userID
            },
            dataType: "json",
            contentType: "application/json"
        }).done(function (res) {
            that.dispatchEvent({
                type: "userDataRecieved",
                data: res
            });
        }).fail(function (code, err) {
            console.log(err);
        });
    }

    function updateUserInformation(userID, rezeptID, date) {
        $.ajax({
            method: "PUT",
            url: backendAdress + "userInformation",
            data: JSON.stringify({
                "userID": userID,
                "date": date,
                "rezeptID": rezeptID
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
        that.getUserInformation = getUserInformation;
        that.updateUserInformation = updateUserInformation;
        return that;
    }

    return init();
};
