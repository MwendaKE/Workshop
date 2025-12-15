// ----------------------------
// GLOBAL VARIABLES
// ----------------------------
const gameBoard = document.getElementById("gameBoard");
const movesElem = document.getElementById("moves");
const timerElem = document.getElementById("timer");

let cards = [];
let firstCard = null;
let secondCard = null;
let lockBoard = false;
let moves = 0;
let matchedPairs = 0;
let timer = 0;
let interval;

// ----------------------------
// START / RESTART GAME
// ----------------------------
function startGame() {
    clearInterval(interval);
    timer = 0;
    moves = 0;
    matchedPairs = 0;
    movesElem.textContent = moves;
    timerElem.textContent = timer;
    firstCard = null;
    secondCard = null;
    lockBoard = false;

    // Example card symbols (8 pairs)
    const symbols = ['🍎','🍌','🍇','🍓','🥝','🍒','🍉','🍑'];
    cards = [...symbols, ...symbols]; // duplicate for pairs
    shuffle(cards);

    // Render cards
    gameBoard.innerHTML = '';
    cards.forEach((symbol, index) => {
        const card = document.createElement('div');
        card.classList.add('card');
        card.dataset.symbol = symbol;
        card.dataset.index = index;
        card.textContent = '';
        card.addEventListener('click', flipCard);
        gameBoard.appendChild(card);
    });

    // Start timer
    interval = setInterval(() => {
        timer++;
        timerElem.textContent = timer;
    }, 1000);
}

// ----------------------------
// SHUFFLE CARDS
// ----------------------------
function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

// ----------------------------
// FLIP CARD
// ----------------------------
function flipCard() {
    if (lockBoard) return;
    if (this === firstCard) return;

    this.classList.add('flipped');
    this.textContent = this.dataset.symbol;

    if (!firstCard) {
        firstCard = this;
    } else {
        secondCard = this;
        lockBoard = true;
        moves++;
        movesElem.textContent = moves;
        checkMatch();
    }
}

// ----------------------------
// CHECK FOR MATCH
// ----------------------------
function checkMatch() {
    if (firstCard.dataset.symbol === secondCard.dataset.symbol) {
        // Match
        firstCard.classList.add('matched');
        secondCard.classList.add('matched');
        matchedPairs++;
        resetBoard();
        if (matchedPairs === cards.length / 2) {
            clearInterval(interval);
            setTimeout(() => alert(`Congratulations! You completed in ${moves} moves and ${timer} seconds.`), 200);
        }
    } else {
        // Not a match, flip back after short delay
        setTimeout(() => {
            firstCard.classList.remove('flipped');
            secondCard.classList.remove('flipped');
            firstCard.textContent = '';
            secondCard.textContent = '';
            resetBoard();
        }, 1000);
    }
}

// ----------------------------
// RESET BOARD POINTERS
// ----------------------------
function resetBoard() {
    [firstCard, secondCard] = [null, null];
    lockBoard = false;
}

// ----------------------------
// INITIALIZE GAME
// ----------------------------
startGame();