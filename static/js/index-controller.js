var app = angular.module("aleatoriedapp", []);

app.controller("indexController", function($scope) {
    $scope.products = ["Milk", "Bread", "Cheese"];
});
