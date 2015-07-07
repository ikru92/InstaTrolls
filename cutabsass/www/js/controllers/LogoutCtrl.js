angular.module('cuControllers').controller('LogoutCtrl', function($scope, Api, $state, $localStorage){
    url = 'http://localhost:8100/api/logout/'
    Api.getApiData(url).then(function(result){
        if(result){
            delete $localStorage.token;
            $state.go('login');
        }
    });
});