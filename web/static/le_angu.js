var myApp = angular.module('myApp', [], function($interpolateProvider) {
 	$interpolateProvider.startSymbol('[['); 
	$interpolateProvider.endSymbol(']]'); 
});

myApp.controller('myCtrl',function($scope) {
	$scope.firstName = 'muxingbang'
});
