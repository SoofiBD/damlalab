$(function () {
	"use strict";

	setTimeout(function () {
		$('.loader_bg').fadeToggle();
	}, 1500);

	$(document).ready(function () {
		$('[data-toggle="tooltip"]').tooltip();
	});

	$(window).on('scroll', function () {
		let scroll = $(window).scrollTop();
		if (scroll >= 100) {
			$("#back-to-top").addClass('b-show_scrollBut');
		} else {
			$("#back-to-top").removeClass('b-show_scrollBut');
		}
	});
	$("#back-to-top").on("click", function () {
		$('body,html').animate({ scrollTop: 0 }, 1000);
	});

	$(".fancybox").fancybox({
		maxWidth: 1200,
		maxHeight: 600,
		width: '70%',
		height: '70%',
	});

	$(document).ready(function () {
		$('#sidebarCollapse').on('click', function () {
			$('#sidebar').toggleClass('active');
			$(this).toggleClass('active');
		});
	});

	$('#blogCarousel').carousel({
		interval: 5000
	});
});
