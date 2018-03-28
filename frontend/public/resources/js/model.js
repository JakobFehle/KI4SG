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
            that.dispatchEvent({
                type: "userDataRecieved",
                data: res
            });
        }).fail(function (code, err) {
            console.log(err);
        });
    }

    function updateUserInformation(rezeptID) {
        $.ajax({
            method: "PUT",
            url: backendAdress + "userInformation",
            data: JSON.stringify({
                "userID": userID,
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
        that.getRecipeBySearch = getRecipeBySearch;
        that.getUserInformation = getUserInformation;
        that.updateUserInformation = updateUserInformation;
        that.setUser = setUser;
        return that;
    }

    return init();
};
