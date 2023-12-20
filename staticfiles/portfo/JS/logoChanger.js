// Image toggler script (Github logo)
function toggleImage() {
  const body = document.body;
  const image = document.getElementById('modeImage');

  if (body.classList.contains('dark-mode')) {
    image.src = '/static/portfo/images/github-mark-white.png';
    image.alt = 'Github';
  } else {
    image.src = '/static/portfo/images/github-mark.png';
    image.alt = 'Github';
  }
}

document.getElementById('dark-mode-toggle').addEventListener('change', toggleImage);
