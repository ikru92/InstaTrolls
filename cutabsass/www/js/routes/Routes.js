angular.module('cuRoutes').config(function($stateProvider, $urlRouterProvider) {

  $stateProvider

      .state('login', {
          url: '/login',
          templateUrl: 'templates/login.html',
          controller: 'LoginCtrl'
      })

      .state('logout', {
        url: '/logout',
        cache:false,
        controller: 'LogoutCtrl'
      })

      .state('tab', {
        url: "/tab",
        abstract: true,
        templateUrl: "templates/tabs.html"
      })

      .state('tab.feeds', {
        url: '/feeds',
        views: {
          'tab-feeds': {
            templateUrl: 'templates/feeds.html',
            controller: 'FeedsCtrl'
          }
        }
      })

      .state('tab.trend', {
          url: '/chats',
          views: {
            'tab-trend': {
              templateUrl: 'templates/tab-chats.html',
              controller: 'TrendCtrl'
            }
          }
        })

        .state('tab.hof', {
          url: '/hof',
          views: {
            'tab-hof': {
              templateUrl: 'templates/tab-dash.html',
              controller: 'HofCtrl'
            }
          }
        })

        .state('tab.comment', {
          url: '/comments/:id',
          views: {
            'tab-feeds': {
              templateUrl: 'templates/comment.html',
              controller: 'CommentCtrl'
            }
          }
        })

      .state('tab.user', {
        url: '/user',
        views: {
          'tab-user': {
            templateUrl: 'templates/tab-users.html',
            controller: 'UserCtrl'
          }
        }
      });

      // if none of the above states are matched, use this as the fallback
      $urlRouterProvider.otherwise('/login');

});
