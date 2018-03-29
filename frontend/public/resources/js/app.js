var NutrFinder = NutrFinder || {};

NutrFinder = (function () {
    "use strict";

    const BACKEND_ADRESS = "http://127.0.0.1:9009/api/";

    var that = {},
        model,
        viewcontroller,
        templateContainer;


    function onSearchButtonClicked(event) {
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

    function onItemClicked(event) {
        viewcontroller.activateModal({
            id: event.data.id,
            title: event.data.title,
            servings: event.data.servings
        });
    }

    function onItemSelectionConfirmed(event) {
        model.updateUserInformation(event.data.id, event.data.propsEaten);
    }

    function onNavUserButtonClicked() {
        model.getUserInformation();
    }

    function onUserInformationRecieved(userInformation) {
        console.log(userInformation.data.data);
        viewcontroller.createUserInformation(userInformation.data.data);
    }

    function initModules() {
        model = new NutrFinder.model(BACKEND_ADRESS);
        viewcontroller = new NutrFinder.viewcontroller({
            navBarElement: document.querySelector("#screenNavBar"),
            navBarTemplate: document.querySelector(templateContainer + " .template-navbar").innerHTML,
            listItemElement: document.querySelector("#screenSearchResults"),
            listItemTemplate: document.querySelector(templateContainer + " .template-create-ListView").innerHTML,
            paginationElement: document.querySelector("#screenPagination"),
            paginationTemplate: document.querySelector(templateContainer + " .template-pagination").innerHTML,
            modalElement: document.querySelector("#screenModal"),
            modalTemplate: document.querySelector(templateContainer + " .template-modal").innerHTML,
            userInformationElement: document.querySelector("#screenUserInformation"),
            userInformationTemplate: document.querySelector(templateContainer + " .template-userInformation").innerHTML
        });

    }

    function initListeners() {
        model.addEventListener("userDataRecieved", onUserInformationRecieved);
        model.addEventListener("userDataUpdated", onUserDataUpdated);
        model.addEventListener("recipeSearchFinished", onRecipeSearchFinished);


        viewcontroller.addEventListener("onSearchButtonClicked", onSearchButtonClicked);
        viewcontroller.addEventListener("onItemClicked", onItemClicked);
        viewcontroller.addEventListener("onItemSelectionConfirmed", onItemSelectionConfirmed);
        viewcontroller.addEventListener("onNavUserButtonClicked", onNavUserButtonClicked);
    }

    function init(templateContainerID) {
        templateContainer = templateContainerID;
        initModules();
        initListeners();
        model.setUser({
            id: 1,
            sex: "M",
            age: 34
        });
    }

    that.init = init;
    return that;
})();
