/*
Api.js is a configuration for API connection between angular and Django
 */

var service = angular.module("apiService", ["ngResource", "ui.bootstrap"]);

service.config(["$httpProvider",
    function (provider) {
        provider.defaults.headers.post["X-CSRFToken"] = getCookie('csrftoken');
    }
]);