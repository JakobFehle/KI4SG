var NutrFinder = NutrFinder || {},
    MMEventTarget = MMEventTarget || {};

NutrFinder.viewcontroller = function (options) {
    "use strict";

    var that = new MMEventTarget(),
        templateSearchBar,
        templateListItem,
        templatePagination,
        templateModal;

    function onSearchButtonClicked() {
        that.dispatchEvent({
            type: "onSearchButtonClicked",
            data: options.searchBarElement.querySelector("#searchField").value
        });
    }

    function activateModal(item) {
        $('#confirmationModal').modal('show');
        options.modalElement.querySelector(".modalRecipeTitle").innerHTML = item.title;
        options.modalElement.querySelector(".modalRecipeTitle").id = item.id;
    }

    function onModalAbort() {
        $('#confirmationModal').modal('hide');
    }

    function onModalConfirm() {
        $('#confirmationModal').modal('hide');
        that.dispatchEvent({
            type: "onItemSelectionConfirmed",
            data: options.modalElement.querySelector(".modalRecipeTitle").id
        });
    }

    function createModal() {
        options.modalElement.innerHTML = templateModal();
        options.modalElement.querySelector(".btn-secondary").addEventListener("click", onModalAbort);
        options.modalElement.querySelector(".btn-primary").addEventListener("click", onModalConfirm);
    }

    function createSearchBar() {
        options.searchBarElement.innerHTML = templateSearchBar();
        options.searchBarElement.querySelector("#searchButton").addEventListener("click", onSearchButtonClicked);
    }

    function resetVisability() {
        var pages = options.listItemElement.querySelectorAll('.newPage');

        _.each(pages, function (page) {
            page.style.display = "none";
        })
    }

    function updateListView(listItems) {
        //        for (var i = 0; i < listItems.length; i++) {
        //            listItems[i].zutaten = listItems[i].zutaten.replace(/[ 0-9.]+[a-zA-Züäö ]*(\:)/gi, " ");
        //            listItems[i].zutaten = listItems[i].zutaten.replace(/([\n])/g, ",");
        //        }

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
        console.log(event.target);
        console.log($(event.target).closest(".list-group-item").find(".listItemTitle"));
        console.log($(event.target).closest(".list-group-item"));
        that.dispatchEvent({
            type: "onItemClicked",
            data: {
                id: event.target.closest(".listItem").id,
                title: $(event.target).closest(".list-group-item").find(".listItemTitle").text()
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
        templateSearchBar = _.template(options.searchBarTemplate);
        templateListItem = _.template(options.listItemTemplate);
        templatePagination = _.template(options.paginationTemplate);
        templateModal = _.template(options.modalTemplate);

        createSearchBar();
        createModal();

        that.activateModal = activateModal;
        that.updateListView = updateListView;
        return that;
    }

    return init();
}
