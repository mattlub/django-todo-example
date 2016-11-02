document.addEventListener("DOMContentLoaded", function() {
  
	// get csrf cookie using jQuery
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	};
  
	var remove_item = function(event) {
		var csrftoken = getCookie('csrftoken');
		var item = this;
		var info = {
			"class": "Remove",
			"id": item.id
		};
		var xhr = new XMLHttpRequest();
		xhr.open("POST", ".");
		xhr.setRequestHeader("X-CSRFToken", csrftoken);
		xhr.send(info);
	};
  
	var remove_buttons = document.getElementsByClassName("remove-button");

	for (var i=0, n=remove_buttons.length; i<n; i++) {
		remove_buttons[i].addEventListener("click", remove_item);
	}

});