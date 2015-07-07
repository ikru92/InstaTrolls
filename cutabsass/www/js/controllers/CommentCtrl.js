angular.module('cuControllers').controller('CommentCtrl', function($scope, 
                                                                   $stateParams, Api,
                                                                   $http,
                                                                   $ionicScrollDelegate,
                                                                   $rootScope){
    $scope.data = null;
    $scope.newComment = {};
    $scope.sendEnable = false
    $rootScope.$on("commentView",function(events,args){
        $scope.indx = args;
    })   
    url = 'http://localhost:8100/api/commentlist/'+$stateParams.id+'/'
    Api.getApiData(url).then(function(result) {
          $scope.data = result;
    })
    $scope.addPhoto = function(){
      angular.element('#CamButton').trigger('click');
    }

    $scope.checkSendEnable = function(file){
        if($scope.newComment.comment || file){
            $scope.sendEnable = true;
        }
        else {
            $scope.sendEnable = false;
        }
    }

    $scope.send=function(){
        $scope.newComment.post = $stateParams.id;
        url = 'http://localhost:8100/api/comment/'
        var formData = new FormData();
        if ($scope.newCommentImg){
            formData.append("new_image", $scope.newCommentImg);
        }
        else{
            $scope.newComment.commentImg = $scope.newCommentImg
        }
        formData.append("new_comment", angular.toJson($scope.newComment));        
        Api.postData(url, formData).then(function(result){
            $scope.data.push(result);
            $scope.newCommentImg = '';
            $scope.newComment.comment='';
            $rootScope.$broadcast("incrementComment",$scope.indx)
            $ionicScrollDelegate.scrollBottom();
        })
    }
});