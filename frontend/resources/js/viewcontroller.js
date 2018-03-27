var NutrFinder = NutrFinder || {},
    MMEventTarget = MMEventTarget || {};

NutrFinder.viewcontroller = function (options) {
    "use strict";

    var that = new MMEventTarget(),
        templateSearchBar,
        templateListItem,
        templatePagination;

    function onSearchButtonClicked() {
        that.dispatchEvent({
            type: "onSearchButtonClicked",
            data: options.searchBarElement.querySelector("#searchField").value
        });
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
        console.log(event.target.closest(".listItem").id);
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
        createSearchBar();
        that.updateListView = updateListView;
        return that;
    }

    return init();
}
