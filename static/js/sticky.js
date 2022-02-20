// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the navbar
var nav_wrapper = document.getElementsByClassName("s1")[0].getElementsByClassName("main-container")[0].getElementsByClassName("intro-wrapper")[0].getElementById("nav_wrapper").innerHTML;

// Get the offset position of the navbar
var sticky = nav_wrapper.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    nav_wrapper.classList.add("sticky")
  } 
  else {
    nav_wrapper.classList.remove("sticky");
  }
}