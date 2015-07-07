angular.module('cuControllers', ['angular-moment','monospaced.elastic', 'ion-affix','ngStorage']);
angular.module('cuDirectives', []);
angular.module('cuServices', []);
angular.module('cuRoutes',[]);
angular.module('cuConfig',['ionic','ngStorage']);

angular.module('cutab', ['cuControllers', 'cuServices', 'cuDirectives',
                         'cuRoutes', 'cuConfig',]);