angular.module('cuConfig').run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    if (window.cordova && window.cordova.plugins && window.cordova.plugins.Keyboard) {
      cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
    }
    if (window.StatusBar) {
      StatusBar.styleLightContent();
    }
  });
});
angular.module('cuConfig').config(function($httpProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.interceptors.push(function($q, $location, $localStorage) {
      return {
              'request': function (config) {
                  config.headers = config.headers || {};
                  if ($localStorage.token) {
                    config.headers.Authorization = 'Token '+$localStorage.token
                  }
                  return config;
              },
              'responseError': function(response) {
                  if(response.status === 401 || response.status === 403) {
                      $location.path('/login');
                  }
                  return $q.reject(response);
              }
      };
  })
});