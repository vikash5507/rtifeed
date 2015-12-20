var screen_width = $(window).width();
if(screen_width < 900){
	$('body').removeClass('fixed');
	$('#search_form').css('display', 'none');
	// alert('done');	
}
else{
	$('.sidebar-toggle').remove();
}