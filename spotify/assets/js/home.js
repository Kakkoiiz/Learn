

const addPlaylist = document.querySelector('.js-add-playlist')
const formPlaylist = document.querySelector('.js-form')
const playlistcontent = document.querySelector('.js-content')
const PlaylistClose = document.querySelector('.js-close')
function showaddPlaylist(){
    formPlaylist.classList.add('open')
    console.log('Button clicked!');
}

function hideaddPlaylist(){
    formPlaylist.classList.remove('open')
}



addPlaylist.addEventListener('click', showaddPlaylist)
PlaylistClose.addEventListener('click', hideaddPlaylist)
formPlaylist.addEventListener('click', hideaddPlaylist)

playlistcontent.addEventListener('click', function (event) {
    event.stopPropagation()

})

// slider

var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  x[slideIndex-1].style.display = "block";  
}



const button = document.querySelector('#myButton');

button.addEventListener('click', () => {
  console.log('Button clicked!');
});