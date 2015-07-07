angular.module('cuControllers').controller('FeedsCtrl', function($scope, Api, $rootScope, $state){

    $scope.data = null;
    $scope.isFullScreen = false;
    url= 'http://localhost:8100/api/feeds/'
    Api.getApiData(url).then(function(result){
        $scope.data = result;
    });
    $rootScope.$on("incrementComment",function(events,args){
      console.log("here");
      $scope.data[args].total_comment++;
    })
    $scope.commentIt = function(id,indx){
      $state.go('tab.comment',{'id':id});
      $rootScope.$broadcast('commentView',indx);
    }
    $scope.loveIt = function(index){
       $scope.love={};
       url = 'http://localhost:8100/api/love/' 
       $scope.love.love_post = $scope.data[index].id;
       Api.postApiData(url,$scope.love).then(function(result){
            $scope.data[index].love++;
       })
    }

    $scope.fullImage = function(){
        $scope.isFullScreen = true;
    }
});