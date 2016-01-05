function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$('#myModal').on('show.bs.modal', function (event) {
	var button = $(event.relatedTarget); // Button that triggered the modal
	var nombre = button.data('whatever'); // Extract info from data-* attributes
	var idmascota = button.data('mascotaid');
	var modal = $(this);
	modal.find('.modal-title').text('¿Desea suscribir a ' + nombre + '?');
	$("#suscribir").click(function(){
	  	$.ajax({
	  		 beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
	    	},
	  		type:"POST",
	  		url: "/mascotas/suscribir?id="+idmascota,
	  		success: function(msg){
	  			modal.modal('hide');
	  			$("#imsuscrito"+idmascota).css('height','20px');
	  			$("#imsuscrito"+idmascota).appendTo("#tdmascota"+idmascota);
	  			alert(msg);
	  		},
	  		error:function(){
			  	alert("failure");
	  		}
	  	});
  	});
});  
$('#myModal2').on('show.bs.modal', function (event) {
	var button = $(event.relatedTarget); // Button that triggered the modal
	var nombre = button.data('whatever'); // Extract info from data-* attributes
	var idmascota = button.data('mascotaid');
	var modal = $(this);
	modal.find('.modal-title').text('¿Desea ingresar a ' + nombre + ' a una atención clínica?');
	var form_consulta = $("#ingresarConsulta");
	form_consulta.submit(function() {
		var data = $(this).serialize()+"&id="+idmascota;
	  	$.ajax({
	  		beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
	    	},
	  		type: "POST",
	  		url:  '/mascotas/ingresar_consulta',
	  		data: data, 
	  		success: function(msg){
	  			modal.modal('hide');
	  			alert(msg);
	  		},
	  		error:function(msg){
			  	alert(msg);
	  		}
	  	});
  	});
});
$('#myModal3').on('show.bs.modal', function (event) {
	var button = $(event.relatedTarget); // Button that triggered the modal
	var nombre = button.data('whatever'); // Extract info from data-* attributes
	var idmascota = button.data('mascotaid');
	var modal = $(this);
	modal.find('.modal-title').text('¿Desea hospitalizar a ' + nombre + '?');
	$("#suscribir").click(function(){
	  	$.ajax({
	  		 beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
	    	},
	  		type:"POST",
	  		url: "/mascotas/suscribir?id="+idmascota,
	  		success: function(msg){
	  			modal.modal('hide');
	  			$("#imsuscrito"+idmascota).appendTo("#tdmascota"+idmascota);
	  			alert(msg);
	  		},
	  		error:function(){
			  	alert("failure");
	  		}
	  	});
  	});
});
$('#myModal4').on('show.bs.modal', function (event) {
	var button = $(event.relatedTarget); // Button that triggered the modal
	var nombre = button.data('whatever'); // Extract info from data-* attributes
	var idmascota = button.data('mascotaid');
	var modal = $(this);
	modal.find('.modal-title').text('¿Desea Reservar una Hora o Ingresar a Peluquería?');
	$('#botonFinReserva').hide();
	$('#botonFinPelu').hide();
    $('#texto_reserva').hide();
    $('#texto_pelu').hide();
	$('#preguntaPelu').show();
	$('#suscribir').click(function(){
	  	$.ajax({
	  		 beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
	    	},
	  		type:"POST",
	  		url: "/mascotas/suscribir?id="+idmascota,
	  		success: function(msg){
	  			modal.modal('hide');
	  			$("#imsuscrito"+idmascota).appendTo("#tdmascota"+idmascota);
	  			alert(msg);
	  		},
	  		error:function(){
			  	alert("failure");
	  		}
	  	});
  	});
});
$('#myModal5').on('show.bs.modal', function (event) {
	var button = $(event.relatedTarget); // Button that triggered the modal
	var nombre = button.data('whatever'); // Extract info from data-* attributes
	var idmascota = button.data('mascotaid');
	var modal = $(this);
	modal.find('.modal-title').text('¿Desea ingresar a hotelería a ' + nombre + '?');
	$("#suscribir").click(function(){
	  	$.ajax({
	  		 beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
	    	},
	  		type:"POST",
	  		url: "/mascotas/suscribir?id="+idmascota,
	  		success: function(msg){
	  			modal.modal('hide');
	  			$("#imsuscrito"+idmascota).appendTo("#tdmascota"+idmascota);
	  			alert(msg);
	  		},
	  		error:function(){
			  	alert("failure");
	  		}
	  	});
  	});
});    