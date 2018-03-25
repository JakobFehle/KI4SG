var NutrFinder = NutrFinder || {};

NutrFinder = (function () {
    "use strict";

    const BACKEND_ADRESS = "http://127.0.0.1:9009/api/";

    var that = {},
        model,
        viewcontroller;


    function onSearchButtonClicked(event) {
        console.log(event.data);
        model.getRecipeBySearch(event.data);
    }

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
        viewcontroller = new NutrFinder.viewcontroller({
            searchButton: document.querySelector("#searchButton"),
            searchField: document.querySelector("#searchField")
        });

    }

    function initListeners() {
        model.addEventListener("userDataRecieved", onUserInformationRecieved);
        model.addEventListener("userDataUpdated", onUserDataUpdated);
        model.addEventListener("recipeSearchFinished", onRecipeSearchFinished);

        viewcontroller.addEventListener("onSearchButtonClicked", onSearchButtonClicked);
    }

    function init() {
        initModules();
        initListeners();
    }

    that.init = init;
    return that;
})();
