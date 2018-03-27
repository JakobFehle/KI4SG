var NutrFinder = NutrFinder || {};

NutrFinder = (function () {
    "use strict";

    const BACKEND_ADRESS = "http://127.0.0.1:9009/api/";

    var that = {},
        model,
        viewcontroller,
        templateContainer;


    function onSearchButtonClicked(event) {
        console.log(event.data);
        model.getRecipeBySearch(event.data);
    }

    function onRecipeSearchFinished(event) {
        viewcontroller.updateListView(event.data.data);
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
            searchBarElement: document.querySelector("#screenSearchBar"),
            searchBarTemplate: document.querySelector(templateContainer + " .template-create-SearchBar").innerHTML,
            listItemElement: document.querySelector("#screenSearchResults"),
            listItemTemplate: document.querySelector(templateContainer + " .template-create-ListView").innerHTML,
            paginationElement: document.querySelector("#screenPagination"),
            paginationTemplate: document.querySelector(templateContainer + " .template-pagination").innerHTML
        });

    }

    function initListeners() {
        model.addEventListener("userDataRecieved", onUserInformationRecieved);
        model.addEventListener("userDataUpdated", onUserDataUpdated);
        model.addEventListener("recipeSearchFinished", onRecipeSearchFinished);

        viewcontroller.addEventListener("onSearchButtonClicked", onSearchButtonClicked);
    }

    function init(templateContainerID) {
        templateContainer = templateContainerID;
        initModules();
        initListeners();
    }

    that.init = init;
    return that;
})();
