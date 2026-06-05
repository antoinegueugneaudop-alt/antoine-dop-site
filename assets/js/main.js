const reelUrl = "https://player.vimeo.com/video/816328344?autoplay=1&title=0&byline=0&portrait=0";
const modal = document.querySelector('[data-reel-modal]');
const frame = document.querySelector('[data-modal-frame]');
const openButtons = document.querySelectorAll('[data-open-reel]');
const closeButton = document.querySelector('[data-close-reel]');
let lastFocusedElement = null;

function openReel(event) {
  lastFocusedElement = event?.currentTarget || document.activeElement;
  frame.innerHTML = `<iframe src="${reelUrl}" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Antoine Gueugneau showreel"></iframe>`;
  modal.classList.add('is-open');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
  closeButton.focus();
}
function closeReel() {
  modal.classList.remove('is-open');
  modal.setAttribute('aria-hidden', 'true');
  frame.innerHTML = '';
  document.body.style.overflow = '';
  lastFocusedElement?.focus();
}

if (modal && frame && closeButton) {
  openButtons.forEach((button) => button.addEventListener('click', openReel));
  closeButton.addEventListener('click', closeReel);
  modal.addEventListener('click', (event) => { if (event.target === modal) closeReel(); });
  document.addEventListener('keydown', (event) => { if (event.key === 'Escape' && modal.classList.contains('is-open')) closeReel(); });
}
