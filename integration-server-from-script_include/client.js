function($scope, $http) {
	
	var c = this;
	
	$('.cep').mask('00000-000');

	$scope.function_search = function(dados) {
		
		var cep = dados['cep'].replace(/\-/g,"");
		var url = "https://viacep.com.br/ws/"+cep+"/json/";
		
		c.data.url = url;
		c.server.update();

	}
}
