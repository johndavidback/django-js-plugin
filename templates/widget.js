// We want this to be an anonymous function
(function() {

	var jQuery;

	if(window.jQuery === undefined) {

		// Grab jquery 1.7.1
		var script = document.createElement('script');
		script.setAttribute('src', 'http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js');

		if(script.readyState) {

			script.onreadystatechange = function() {
				if(this.readyState == 'complete' || this.readyState == 'loaded') {
					scriptLoadHandler();
				}
			};
		} else {
			script.onload = scriptLoadHandler;
		}

		// Append to the <head> if it's found, otherwise the doc root
		(document.getElementsByTagName("head")[0] || document.documentElement).appendChild(script);

	} else {
		// This means jQuery is already in the DOM
		jQuery = window.jQuery;

		begin();
	}

	function scriptLoadHandler() {
		// We want our jQuery to be the one we loaded

		jQuery = window.jQuery.noConflict(true);

		begin();
	}

	function begin() {

		jQuery('#plugin-root').html('Hey there, {{ name }} with account {{ account_id }}');

	}


})();

