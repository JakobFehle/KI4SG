var NutrFinder = NutrFinder || {};

NutrFinder = (function () {
    "use strict";

    const BACKEND_ADRESS = "http://127.0.0.1:9009/api/";

    var that = {},
        model;


    function onRecipeSearchFinished(event) {
        console.log(event.data);
    }

    function onUserInformationRecieved(event) {
        console.log(event.data);
    }

    function onUserDataUpdated(event) {
        console.log(event.data);
    }

    function initModules() {
        model = new NutrFinder.model(BACKEND_ADRESS);
    }

    function initListeners() {
        model.addEventListener("userDataRecieved", onUserInformationRecieved);
        model.addEventListener("userDataUpdated", onUserDataUpdated);
        model.addEventListener("recipeSearchFinished", onRecipeSearchFinished);
    }

    function init() {
        initModules();
        initListeners();
    }

    that.init = init;
    return that;
})();
