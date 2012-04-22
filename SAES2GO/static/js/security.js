$(document).ready(function (){

	
	$("#frmLogIn").submit(function () {
		var $usuario = $("#logUser")
		var $pass = $("#logPass")
		if($usuario.val() == ""){	
			$usuario .css("background-color","#F6F0AB")
			return false;
		}

		if($pass.val() == ""){	
			$pass .css("background-color","#F6F0AB")
			return false;
		}

		return true;
	});


    $.fn.serializeObject = function () {
        var o = {};        
        var a = this.serializeArray();

        $.each(a, function () {
            if (o[this.name] !== undefined) {
                if (!o[this.name].push) {
                    o[this.name] = [o[this.name]];
                }
                o[this.name].push(this.value || '');
            }
            else {
                o[this.name] = this.value || '';
            }
        });

        return o;
    };

});