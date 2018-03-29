var NutrFinder = NutrFinder || {},
    MMEventTarget = MMEventTarget || {};

NutrFinder.viewcontroller = function (options) {
    "use strict";

    var that = new MMEventTarget(),
        templateNavBar,
        templateListItem,
        templatePagination,
        templateModal,
        templateUserInformation;


    function createUserInformation(userInformation) {
        options.userInformationElement.innerHTML = templateUserInformation(userInformation);
        options.userInformationElement.style.display = "block";
    }

    function onSearchButtonClicked() {
        onNavSearchResultsClicked(); // Visability
        that.dispatchEvent({
            type: "onSearchButtonClicked",
            data: options.navBarElement.querySelector("#searchField").value
        });
    }

    function activateModal(item) {
        $('#confirmationModal').modal('show');
        options.modalElement.querySelector(".modalRecipeTitle").innerHTML = item.title;
        options.modalElement.querySelector(".modalRecipeTitle").id = item.id;
        options.modalElement.querySelector(".modalRecipeServings").innerHTML = item.servings;
    }

    function onModalAbort() {
        $('#confirmationModal').modal('hide');
    }

    function onModalConfirm() {
        $('#confirmationModal').modal('hide');
        var proportionsEaten = parseInt($(options.modalElement).find("option:selected").val()) / parseInt(options.modalElement.querySelector('.modalRecipeServings').innerHTML);
        that.dispatchEvent({
            type: "onItemSelectionConfirmed",
            data: {
                id: options.modalElement.querySelector(".modalRecipeTitle").id,
                propsEaten: proportionsEaten
            }
        });
    }

    function createModal() {
        options.modalElement.innerHTML = templateModal();
        options.modalElement.querySelector(".btn-secondary").addEventListener("click", onModalAbort);
        options.modalElement.querySelector(".btn-primary").addEventListener("click", onModalConfirm);
    }

    function onNavUserButtonClicked(event) {
        $("#navBarSearchResultsButton").closest('.nav-item').removeClass('active');
        $("#navBarUserButton").closest('.nav-item').addClass('active');
        resetVisability();
        that.dispatchEvent({
            type: "onNavUserButtonClicked"
        });
    }

    function onNavSearchResultsClicked(event) {
        $("#navBarSearchResultsButton").closest('.nav-item').addClass('active');
        $("#navBarUserButton").closest('.nav-item').removeClass('active');
        resetVisability();
        options.paginationElement.style.display = "block";
        options.listItemElement.style.display = "block";
    }

    function createNavBar() {
        options.navBarElement.innerHTML = templateNavBar();
        options.navBarElement.querySelector("#searchButton").addEventListener("click", onSearchButtonClicked);
        options.navBarElement.querySelector("#navBarUserButton").addEventListener("click", onNavUserButtonClicked);
        options.navBarElement.querySelector("#navBarSearchResultsButton").addEventListener("click", onNavSearchResultsClicked);
    }

    function resetPageVisability() {
        _.each(options.listItemElement.querySelectorAll('.newPage'), function (page) {
            page.style.display = "none";
        });
        options.userInformationElement.innerHTML = null;
    }

    function resetVisability() {
        options.paginationElement.style.display = "none";
        options.listItemElement.style.display = "none";
        options.userInformationElement.style.display = "none";
    }

    function updateListView(listItems) {
        for (var i = 0; i < listItems.length; i++) {
            //                    listItems[i].zutaten = listItems[i].zutaten.replace(/[ 0-9.]+[a-zA-Züäö ]*(\:)/gi, " ");
            //                    listItems[i].zutaten = listItems[i].zutaten.replace(/([\n])/g, ",");
            listItems[i].zutaten = listItems[i].zutaten.replace(/[:]/g, " ");
            listItems[i].zutaten = listItems[i].zutaten.replace(/[\n]/g, ";");
        }

        options.listItemElement.innerHTML = templateListItem({
            items: listItems
        });
        updatePagination();
    }

    function updatePagination() {
        var pages = options.listItemElement.querySelectorAll(".newPage");
        options.paginationElement.innerHTML = templatePagination({
            count: pages.length
        })
        wireGUIListener();
    }

    function onPageSelected(event) {
        resetVisability()
        options.listItemElement.querySelector('#page' + $.trim(event.target.firstChild.data)).style.display = "block";
    }

    function onItemSelected(event) {
        that.dispatchEvent({
            type: "onItemClicked",
            data: {
                id: event.target.closest(".listItem").id,
                title: $(event.target).closest(".list-group-item").find(".listItemTitle").text(),
                servings: $(event.target).closest(".list-group-item").find(".listItemServings").text()
            }
        });
    }

    function wireGUIListener() {
        var pages = options.paginationElement.querySelectorAll('.page-link'),
            listItems = options.listItemElement.querySelectorAll('.list-group-item');

        _.each(pages, function (page) {
            page.addEventListener("click", onPageSelected);
        });

        _.each(listItems, function (item) {
            item.addEventListener("click", onItemSelected);
        });
    }

    function init() {
        templateNavBar = _.template(options.navBarTemplate);
        templateListItem = _.template(options.listItemTemplate);
        templatePagination = _.template(options.paginationTemplate);
        templateModal = _.template(options.modalTemplate);
        templateUserInformation = _.template(options.userInformationTemplate);

        createNavBar();
        createModal();

        that.createUserInformation = createUserInformation;
        that.activateModal = activateModal;
        that.updateListView = updateListView;
        return that;
    }

    return init();
}
