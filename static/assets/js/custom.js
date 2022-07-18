(function($) {

	$(document).ready(function() {
	  $('body').addClass('js');
	  var $menu = $('#menu'),
	    $menulink = $('.menu-link');
	  
	$menulink.click(function() {
	  $menulink.toggleClass('active');
	  $menu.toggleClass('active');
	  return false;
	});});


	videoPopup();


	$('.owl-carousel').owlCarousel({
	    loop:true,
		margin:10,
		autoWidth:false,
		nav:true,
	    autoplay:true,
		// navText : ['<i class="fa fa-angle-left" aria-hidden="true"></i>','<i class="fa fa-angle-right" aria-hidden="true"></i>'],
		autoplayTimeout:2000,
		autoplayHoverPause:true,
	    responsive:{
	        0:{
	            items:1
	        },
	        550:{
	            items:1
	        },
	        750:{
	            items:1
	        },
	        1000:{
	            items:1
	        },
	        1200:{
	            items:1
	        }
	    }
	})


	$(".Modern-Slider").slick({
	    autoplay:true,
	    autoplaySpeed:10000,
	    speed:600,
	    slidesToShow:1,
	    slidesToScroll:1,
	    pauseOnHover:false,
	    dots:true,
	    pauseOnDotsHover:true,
	    cssEase:'fade',
	   // fade:true,
	    draggable:false,
	    prevArrow:'<button class="PrevArrow"></button>',
	    nextArrow:'<button class="NextArrow"></button>', 
	});


	$("div.features-post").hover(
	    function() {
	        $(this).find("div.content-hide").slideToggle("medium");
	    },
	    function() {
	        $(this).find("div.content-hide").slideToggle("medium");
	    }
	 );


	$( "#tabs" ).tabs();



})(jQuery);