// ---------------------
// Simple Auto Carousel
// ---------------------
// Behavior:
// - auto-advance every 1000ms (1s)
// - dots navigation (clickable)
// - pause on hover (mouse enter) and resume on leave
// - clicking a dot jumps to that slide and resets auto-advance timer

// Grab elements
const slidesEl = document.getElementById('slides');
const dotsEl   = document.getElementById('dots');
const carousel = document.getElementById('carousel');
const pauseIndicator = document.getElementById('pauseIndicator');

// Collect slide elements and count
const slideElements = Array.from(slidesEl.getElementsByClassName('slide'));
const totalSlides = slideElements.length;

// state
let index = 0;                  // current slide index (0-based)
const INTERVAL_MS = 1000;       // change every 1 second
let timerId = null;             // will store setInterval id
let isPaused = false;           // whether carousel is paused

// --- Create dots dynamically based on slide count ---
for (let i = 0; i < totalSlides; i++) {
  const dot = document.createElement('div');
  dot.className = 'dot';
  // Clicking a dot moves to that slide
  dot.addEventListener('click', () => {
    goToSlide(i);
    restartTimer(); // reset auto-advance so user has time to view
  });
  dotsEl.appendChild(dot);
}

// helper: update active dot class
function updateDots() {
  const dots = dotsEl.children;
  for (let i = 0; i < dots.length; i++) {
    dots[i].classList.toggle('active', i === index);
  }
}

// helper: move slides wrapper to show current slide
function updateSlidePosition() {
  // translateX by -index * 100%
  slidesEl.style.transform = `translateX(-${index * 100}%)`;
  updateDots();
}

// go to specific slide index
function goToSlide(i) {
  if (i < 0) i = 0;
  if (i >= totalSlides) i = totalSlides - 1;
  index = i;
  updateSlidePosition();
}

// advance to next slide (loops)
function nextSlide() {
  index = (index + 1) % totalSlides;
  updateSlidePosition();
}

// start automatic sliding
function startTimer() {
  if (timerId) return; // already running
  timerId = setInterval(nextSlide, INTERVAL_MS);
}

// stop automatic sliding
function stopTimer() {
  if (!timerId) return;
  clearInterval(timerId);
  timerId = null;
}

// restart timer (stop then start) — useful after manual navigation
function restartTimer() {
  stopTimer();
  startTimer();
}

// pause (called on mouseenter)
function pauseCarousel() {
  if (isPaused) return;
  isPaused = true;
  stopTimer();
  pauseIndicator.classList.add('visible');
}

// resume (called on mouseleave)
function resumeCarousel() {
  if (!isPaused) return;
  isPaused = false;
  pauseIndicator.classList.remove('visible');
  startTimer();
}

// Pause on hover (desktop) and on touchstart for mobile friendliness
carousel.addEventListener('mouseenter', pauseCarousel);
carousel.addEventListener('mouseleave', resumeCarousel);

// For touch devices, pause on touchstart and resume on touchend
carousel.addEventListener('touchstart', pauseCarousel, {passive: true});
carousel.addEventListener('touchend', resumeCarousel, {passive: true});

// initialize: show first slide and start auto-advance
updateSlidePosition();
startTimer();