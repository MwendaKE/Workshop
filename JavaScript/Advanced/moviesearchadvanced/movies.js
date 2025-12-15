const API_KEY = "";

const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const moviesContainer = document.getElementById("moviesContainer");
const typeFilter = document.getElementById("typeFilter");
const yearFilter = document.getElementById("yearFilter");
const pagination = document.getElementById("pagination");

const modal = document.getElementById("movieModal");
const modalClose = document.getElementById("modalClose");
const modalTitle = document.getElementById("modalTitle");
const modalPoster = document.getElementById("modalPoster");
const modalYear = document.getElementById("modalYear");
const modalGenre = document.getElementById("modalGenre");
const modalPlot = document.getElementById("modalPlot");
const modalDirector = document.getElementById("modalDirector");
const modalActors = document.getElementById("modalActors");
const addFavoriteBtn = document.getElementById("addFavoriteBtn");
const favoritesContainer = document.getElementById("favorites");

let currentMovies = [];
let currentPage = 1;
let totalPages = 1;
let lastSearch = "";
let lastType = "";
let lastYear = "";
let currentMovieID = null;

// ----------------------------
// SEARCH MOVIES
// ----------------------------
async function searchMovies(query, page = 1, type = "", year = "") {
    try {
        lastSearch = query;
        lastType = type;
        lastYear = year;
        currentPage = page;

        let url = `https://www.omdbapi.com/?s=${query}&apikey=${API_KEY}&page=${page}`;
        if(type) url += `&type=${type}`;
        if(year) url += `&y=${year}`;

        const response = await fetch(url);
        const data = await response.json();

        if(data.Response === "False") {
            moviesContainer.innerHTML = `<p style="text-align:center; width:100%;">${data.Error}</p>`;
            pagination.innerHTML = "";
            return;
        }

        currentMovies = data.Search;
        totalPages = Math.ceil(data.totalResults / 10);

        displayMovies(currentMovies);
        displayPagination();
    } catch(err) {
        console.error("Error fetching movies:", err);
    }
}

// ----------------------------
// DISPLAY MOVIES
// ----------------------------
function displayMovies(movies) {
    moviesContainer.innerHTML = "";

    movies.forEach(movie => {
        const card = document.createElement("div");
        card.classList.add("movie-card");

        card.innerHTML = `
            <img src="${movie.Poster !== "N/A"?movie.Poster:"https://via.placeholder.com/180x270?text=No+Image"}" alt="${movie.Title}">
            <h4>${movie.Title}</h4>
            <p>Year: ${movie.Year}</p>
        `;

        card.addEventListener("click", () => getMovieDetails(movie.imdbID));
        moviesContainer.appendChild(card);
    });
}

// ----------------------------
// PAGINATION
// ----------------------------
function displayPagination() {
    pagination.innerHTML = "";
    for(let i=1;i<=totalPages;i++){
        const btn = document.createElement("button");
        btn.textContent = i;
        if(i===currentPage) btn.classList.add("disabled");
        btn.addEventListener("click",()=>searchMovies(lastSearch,i,lastType,lastYear));
        pagination.appendChild(btn);
    }
}

// ----------------------------
// DETAILED INFO
// ----------------------------
async function getMovieDetails(imdbID) {
    try {
        const response = await fetch(`https://www.omdbapi.com/?i=${imdbID}&apikey=${API_KEY}`);
        const data = await response.json();

        modalTitle.textContent = data.Title;
        modalPoster.src = data.Poster !== "N/A" ? data.Poster : "";
        modalYear.textContent = `Year: ${data.Year}`;
        modalGenre.textContent = `Genre: ${data.Genre}`;
        modalPlot.textContent = `Plot: ${data.Plot}`;
        modalDirector.textContent = `Director: ${data.Director}`;
        modalActors.textContent = `Actors: ${data.Actors}`;
        currentMovieID = imdbID;

        modal.style.display = "flex";
    } catch(err) { console.error(err); }
}

// ----------------------------
// FAVORITES
// ----------------------------
function loadFavorites() {
    const favs = JSON.parse(localStorage.getItem("favorites")||"[]");
    favoritesContainer.innerHTML = "";
    favs.forEach(fav=>{
        const div = document.createElement("div");
        div.classList.add("favorite-card");
        div.innerHTML = `<img src="${fav.Poster}" alt="${fav.Title}"><p>${fav.Title}</p>
        <button onclick='removeFavorite("${fav.imdbID}")'>Remove</button>`;
        favoritesContainer.appendChild(div);
    });
}

function addFavorite() {
    const favs = JSON.parse(localStorage.getItem("favorites")||"[]");
    if(favs.find(f=>f.imdbID===currentMovieID)) return alert("Already in favorites!");
    const movie = currentMovies.find(m=>m.imdbID===currentMovieID);
    if(movie){
        favs.push(movie);
        localStorage.setItem("favorites", JSON.stringify(favs));
        loadFavorites();
        alert("Added to favorites!");
    }
}

function removeFavorite(id){
    let favs = JSON.parse(localStorage.getItem("favorites")||"[]");
    favs = favs.filter(f=>f.imdbID!==id);
    localStorage.setItem("favorites", JSON.stringify(favs));
    loadFavorites();
}

// ----------------------------
// EVENT LISTENERS
// ----------------------------
searchBtn.addEventListener("click", ()=>{
    const query = searchInput.value.trim();
    const type = typeFilter.value;
    const year = yearFilter.value.trim();
    if(query) searchMovies(query,1,type,year);
});

searchInput.addEventListener("keypress",(e)=>{
    if(e.key==="Enter") searchBtn.click();
});

modalClose.addEventListener("click",()=>{ modal.style.display="none"; });
window.addEventListener("click",(e)=>{ if(e.target===modal) modal.style.display="none"; });

addFavoriteBtn.addEventListener("click",addFavorite);

// Load favorites on page load
loadFavorites();
