var images = [
    { url: 'images/elits-president.png', width: '305px' },
    { url: 'images/elits-1st-year-rep.png', width: '310px' },
    { url: 'images/elits-2nd-year-rep.png', width: '325px' },
    // Add more image URLs and widths as needed
  ];

  // Function to set random image for elits-member
function setRandomImage() {
var randomIndex = Math.floor(Math.random() * images.length);
var randomImage = images[randomIndex];
document.querySelector('.elits-member').src = randomImage.url;
document.querySelector('.elits-member').style.width = randomImage.width;
}

// Call the function when the page loads and reloads
window.onload = setRandomImage;
window.onbeforeunload = setRandomImage; // For modern browsers
window.onunload = setRandomImage; 
