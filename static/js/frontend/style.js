var Frontend = function() {
	var loading = function(){
		$('body').removeClass('preloading');
    	$('#preload').hide();
	}
    return {
        init: function(){
        	loading();
        }
    }
}();

$(document).ready(function() {
    Frontend.init();
})
