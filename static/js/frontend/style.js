$(window).load(function(){
    $('body').removeClass('preloading');
    $('#preload').hide();

 //    $("a[href='#top']").click(function() {
	// 	$("html, body").animate({ scrollTop: 0 }, "slow");
	// 	return false;
	// });
	$(".tp-rightarrow").html('<i class="fa fa-chevron-right" aria-hidden="true"></i>');
	$(".tp-lefttarrow").html('<i class="fa fa-chevron-left" aria-hidden="true"></i>');
})