const questionContainer = document.getElementById("questionContainer");
const scoreContainer = document.getElementById("scoreContainer");
const timerEl = document.getElementById("timer");
const categorySelect = document.getElementById("category");
const restartBtn = document.getElementById("restartBtn");

let quiz = [];
let currentQuestionIndex = 0;
let score = 0;
let timeLeft = 60;
let timerInterval = null;
let questionData = {};

// ----------------------------
// LOAD QUESTIONS FROM JSON
// ----------------------------
async function loadQuestions(){
    try {
        const response = await fetch('questions.json');
        questionData = await response.json();
    } catch(err){
        alert("Failed to load questions. Make sure questions.json is available.");
        console.error(err);
    }
}

// ----------------------------
// START QUIZ
// ----------------------------
function startQuiz(){
    const selectedCategory = categorySelect.value;
    if(!selectedCategory) return alert("Please select a category");

    quiz = [...questionData[selectedCategory]]; // copy questions
    shuffleArray(quiz);
    currentQuestionIndex = 0;
    score = 0;
    timeLeft = 60;
    scoreContainer.textContent = "";
    restartBtn.style.display = "none";

    showQuestion();
    startTimer();
}

// ----------------------------
// TIMER
// ----------------------------
function startTimer(){
    clearInterval(timerInterval);
    timerInterval = setInterval(()=>{
        timeLeft--;
        timerEl.textContent = `Time: ${timeLeft}s`;
        if(timeLeft <=0){
            clearInterval(timerInterval);
            showScore();
        }
    },1000);
}

// ----------------------------
// SHOW QUESTION
// ----------------------------
function showQuestion(){
    if(currentQuestionIndex >= quiz.length){
        clearInterval(timerInterval);
        showScore();
        return;
    }

    const q = quiz[currentQuestionIndex];
    questionContainer.innerHTML = `<div class="question">${q.question}</div>`;
    const optionsDiv = document.createElement("div");
    optionsDiv.classList.add("options");

    q.options.forEach(option=>{
        const btn = document.createElement("button");
        btn.textContent = option;
        btn.addEventListener("click", ()=>{
            checkAnswer(btn, option);
        });
        optionsDiv.appendChild(btn);
    });

    questionContainer.appendChild(optionsDiv);
}

// ----------------------------
// CHECK ANSWER
// ----------------------------
function checkAnswer(btn, selected){
    const q = quiz[currentQuestionIndex];
    Array.from(btn.parentElement.children).forEach(b=>{
        if(b.textContent === q.answer) b.classList.add("correct");
        if(b.textContent !== q.answer && b.textContent===selected) b.classList.add("wrong");
        b.disabled = true;
    });

    if(selected === q.answer) score++;

    setTimeout(()=>{
        currentQuestionIndex++;
        showQuestion();
    },1000);
}

// ----------------------------
// SHOW SCORE
// ----------------------------
function showScore(){
    questionContainer.innerHTML = `<h3>Quiz Completed!</h3>`;
    scoreContainer.textContent = `Your Score: ${score} / ${quiz.length}`;
    restartBtn.style.display = "block";
}

// ----------------------------
// RESTART QUIZ
// ----------------------------
restartBtn.addEventListener("click", startQuiz);
categorySelect.addEventListener("change", startQuiz);

// ----------------------------
// HELPER: SHUFFLE ARRAY
// ----------------------------
function shuffleArray(array){
    for(let i=array.length-1;i>0;i--){
        const j = Math.floor(Math.random()*(i+1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

// ----------------------------
// INIT
// ----------------------------
loadQuestions();