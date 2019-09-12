var APICorreios = Class.create();

APICorreios.prototype = Object.extendsObject(AbstractAjaxProcessor, {
	
	correios: function(url) {

		try {
			
			var request = new sn_ws.RESTMessageV2();
			
			request.setHttpMethod('get');
			request.setEndpoint(url);
			request.setRequestHeader("Content-Type", "application/json");
			request.setRequestHeader("Accept", "application/json");

			var response = request.execute();
			var httpStatus = response.getStatusCode();

			if (httpStatus == 200) {       
				
				var responseBody = response.getBody();
				var json = JSON.parse(responseBody);
				var responseAPI = {
					cep: json['cep'],
					logradouro: json['logradouro'],
					complemento: json['complemento'],
					bairro: json['bairro'],
					localidade: json['localidade'],
					uf: json['uf'],
					unidade: json['unidade'],
					ibge: json['ibge'],
					gia: json['gia']
					
				}
				
			}
			
		} catch(ex) {
			
			var message = ex.getMessage();
			gs.addErrorMessage(message);
			gs.debug(message);
			
		}

		return responseAPI;
		
	}
	
});