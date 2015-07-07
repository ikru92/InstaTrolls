angular.module('cuServices', [])

.service('Api', function($http, $q, $state) {
  this.getApiData = function(url) {
    var q = $q.defer();
    $http.get(url)
    .success(function(data) {
      q.resolve(data);
    })
    .error(function(error,status){
      if (status == 403)
        $state.go('login');
      q.reject(error);
    })
    return q.promise;
  }
  this.postApiData = function(url, postData) {
    var q = $q.defer();
    $http.post(url, postData)
    .success(function(data) {
      q.resolve(data);
    })
    .error(function(error){
      q.reject(error);
    })
    return q.promise;
  }
  this.postData = function(url, postData) {
    var q = $q.defer();
    $http.post(
            url, postData,{
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined}}
        )
    .success(function(data) {
      q.resolve(data);
    })
    .error(function(error){
      q.reject(error);
    })
    return q.promise;
  }
})