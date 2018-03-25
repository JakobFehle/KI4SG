var NutrFinder = NutrFinder || {},
    MMEventTarget = MMEventTarget || {};

NutrFinder.viewcontroller = function (options) {
    "use strict";

    var that = new MMEventTarget();

    function onSearchButtonClicked() {
        that.dispatchEvent({
            type: "onSearchButtonClicked",
            data: options.searchField.value
        })
    }

    function wireGUIListener() {
        options.searchButton.addEventListener("click", onSearchButtonClicked);
    }

    function init() {
        wireGUIListener();

        return that;
    }

    return init();
}
