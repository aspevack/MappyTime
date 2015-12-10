$(document).ready(function(){	

	$('#url_short').on('input', function(){
		var input = $(this);
		var REGEX = /^[a-zA-Z]+$/;
		var isLetters = REGEX.test(input.val());
		if (isLetters) {
			input.removeClass("invalid").addClass("valid");
			$('btn-default').prop('disabled', false);
			$("#url_short").siblings("span").removeClass("error_show").addClass("error");
		}
		else {
			input.removeClass("valid").addClass("invalid");
			$('btn-default').prop('disabled', true);
			$("#url_short").siblings("span").removeClass("error").addClass("error_show");
		}
	});

	$("#url_submit btn-default-default").click(function(event){
		//need to edit this for file upload
		var form_data=$("#urlshortener").serializeArray();
		var error_free=true;
		for (var input in form_data){
			var element=$("#url_"+form_data[input]['name']);
			var valid=element.hasClass("valid");
			var error_element=$("span", element.parent());
			if (!valid){
				error_element.removeClass("error").addClass("error_show"); 
				error_free=false;
				console.log(error_element)
			}
			else{
				error_element.removeClass("error_show").addClass("error");
			}
		}
		if (!error_free){
			event.preventDefault(); 
		}
	});
});


