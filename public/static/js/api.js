/*
Api.js is a configuration for API connection between angular and Django
 */

function init_app_ng(app){
// Cambiando el simbolo {{ a [[
app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
});
// Agregando header X-Requested-With para soportar is_ajax de django
app.config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

app.config(["$httpProvider",
    function (provider) {
        provider.defaults.headers.post["X-CSRFToken"] = getCookie('csrftoken');
    }
]);
}