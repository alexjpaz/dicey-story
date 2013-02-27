(function() {
	var route = angular.module('Route', []);
	
    route.config(['$routeProvider', function($routeProvider) {
    	
    	$routeProvider.when('/derp', {});
		}])

		
	route.controller('RouteCtrl', function() {
		
	});
})();