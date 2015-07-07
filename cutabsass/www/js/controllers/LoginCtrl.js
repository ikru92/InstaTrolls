angular.module('cuControllers').controller('LoginCtrl', function($scope, Api, $state, $localStorage){

    $scope.message = false;
    $scope.user = {};
    $scope.doLogin = function() {
        if ($localStorage.token){
            $state.go('tab.feeds'); 
        }
        else{
            url = 'http://localhost:8100/api/auth'
            Api.postApiData(url,$scope.user).then(function(result){
                $scope.user = {};
                $localStorage.token = result;
                if (result)
                    $state.go('tab.feeds'); 
                else 
                    $scope.message = true;      
            });
        }
    };
});
