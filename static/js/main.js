

//   ===================== JQUERY ==================== */
'use strict';

   /*------------------Preloader--------------------*/
   $(window).on('load', function () {
       $(".loader").fadeOut();
       $("#preloder").delay(500).fadeOut("slow");

   });


$(document).ready(function(){


   $('.count').each(function() {
      var $this = $(this),
         countTo = $this.attr('data-count');
      $({ countNum: $this.text()}).animate({
      countNum: countTo
      },
      {
      duration: 5000,
      step: function() {
         $this.text(Math.floor(this.countNum));
      },
      complete: function() {
         $this.text(this.countNum + '+');
      }
      });
   });

});









let navbar = document.querySelector('.header .navbar');
let searchForm = document.querySelector('.header .search-form');
let loginForm = document.querySelector('.header .login-form');
let contactInfo = document.querySelector('.contact-info');

// info = document.getElementsByClassName("btns");
//     for (var i = 0; i < info.length; i++) {
//         info[i].addEventListener("click", function () {
//              contactInfo.classList.add('active');
//         });
//     }

document.querySelector('#menu-btn').onclick = () =>{
   navbar.classList.toggle('active');
   searchForm.classList.remove('active');
   loginForm.classList.remove('active');
};

document.querySelector('#search-btn').onclick = () =>{
   searchForm.classList.toggle('active');
   navbar.classList.remove('active');
   loginForm.classList.remove('active');
};

document.querySelector('#login-btn').onclick = () =>{
   loginForm.classList.toggle('active');
   navbar.classList.remove('active');
   searchForm.classList.remove('active'); 
};

document.querySelector('#info-btn').onclick = () =>{
   contactInfo.classList.add('active');
}


document.querySelector('#close-contact-info').onclick = () =>{
   contactInfo.classList.remove('active');
}

window.onscroll = () =>{
   navbar.classList.remove('active');
   searchForm.classList.remove('active');
   loginForm.classList.remove('active');
}

var swiper = new Swiper(".home-slider", {
   loop:true,
   grabCursor:true,
   navigation: {
     nextEl: ".swiper-button-next",
     prevEl: ".swiper-button-prev",
   },
});

document.getElementById("year").innerHTML = new Date().getFullYear();


