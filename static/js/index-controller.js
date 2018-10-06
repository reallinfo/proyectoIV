var app = angular.module('aleatoriedapp', []);

app.controller('indexController', ['$scope', '$http', function($scope, $http) {
    $scope.random_n = 0;
    $scope.min_n = 0;
    $scope.max_n = 100000;
    $scope.error = '';
    // var addr = 'https://aleatoriedapp.herokuapp.com';
    var addr = 'http://localhost:8000';

    $scope.getRandomN = function() {
        $scope.random_n = 0;
        $scope.error = '';
        var params = {
            min: $scope.min_n,
            max: $scope.max_n
        };

        $http({
            method: 'GET',
            url: addr + '/random/random_number',
            params: params
        }).then(function(response) {
            $scope.random_n = response.data.random_number;
        }, function (response) {
            $scope.error = response.data.error;
        });
    };

    $scope.random_n = $scope.getRandomN();
}]);
