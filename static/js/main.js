jQuery(document).ready(function(){
	if( $('.cd-stretchy-nav').length > 0 ) {
		var stretchyNavs = $('.cd-stretchy-nav');
		
		stretchyNavs.each(function(){
			var stretchyNav = $(this),
				stretchyNavTrigger = stretchyNav.find('.cd-nav-trigger');
			
			stretchyNavTrigger.on('click', function(event){
				event.preventDefault();
				stretchyNav.toggleClass('nav-is-visible');
			});
		});

		$(document).on('click', function(event){
			( !$(event.target).is('.cd-nav-trigger') && !$(event.target).is('.cd-nav-trigger span') ) && stretchyNavs.removeClass('nav-is-visible');
		});
	}
});
$(function() {
    var header = $(".navn");
    $(window).scroll(function() {    
        var scroll = $(window).scrollTop();
    
        if (scroll >= 150) {
            header.addClass("navscroll");
        } else {
            header.removeClass("navscroll");
        }
    });
});
$(function() {
    var header = $(".navbar-brand");
    $(window).scroll(function() {    
        var scroll = $(window).scrollTop();
    
        if (scroll >= 150) {
            header.addClass("navbarbrandscroll");
        } else {
            header.removeClass("navbarbrandscroll");
        }
    });
});