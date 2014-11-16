/* Starting login app */
var url_ajax = null;
var url_authentication = null;

login_app = angular.module("login",[]);

init_app_ng(login_app);


login_app.controller("LoginController",function($scope,$http){
    $scope.dataForm = {};
    $scope.doClick = function(){
        response = $http.post(url_authentication,$scope.dataForm)
            .success(function(data, status, headers, config){
             if(data.done){
                 location.href = data.redirect;
             }
        })
            .error(function(data, status, headers, config){
            $('#username,#passwd').addClass()
        });
    }
});
