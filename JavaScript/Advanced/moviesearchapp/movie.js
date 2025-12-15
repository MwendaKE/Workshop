// Replace with your OMDb API key
const API_KEY = "YOUR_API_KEY";

// Elements
const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");
const moviesContainer = document.getElementById("moviesContainer");

const modal = document.getElementById("movieModal");
const modalClose = document.getElementById("modalClose");
const modalTitle = document.getElementById("modalTitle");
const modalPoster = document.getElementById("modalPoster");
const modalYear = document.getElementById("modalYear");
const modalGenre = document.getElementById("modalGenre");
const modalPlot = document.getElementById("modalPlot");
const modalDirector = document.getElementById("modalDirector");
const modalActors = document.getElementById("modalActors");

// ----------------------------
// SEARCH MOVIES
// ----------------------------
async function searchMovies(query) {
    try {
        const response = await fetch(`https://www.omdbapi.com/?s=${query}&apikey=${API_KEY}`);
        const data = await response.json();

        if (data.Response === "False") {
            moviesContainer.innerHTML = `<p style="text-align:center; width:100%;">${data.Error}</p>`;
            return;
        }

        displayMovies(data.Search);
    } catch (err) {
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
            <img src="${movie.Poster !== "N/A" ? movie.Poster : "https://via.placeholder.com/180x270?text=No+Image"}" alt="${movie.Title}">
            <h4>${movie.Title}</h4>
            <p>Year: ${movie.Year}</p>
        `;

        // Click to show detailed info
        card.addEventListener("click", () => getMovieDetails(movie.imdbID));

        moviesContainer.appendChild(card);
    });
}

// ----------------------------
// GET DETAILED MOVIE INFO
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

        modal.style.display = "flex";
    } catch (err) {
        console.error("Error fetching movie details:", err);
    }
}

// ----------------------------
// EVENT LISTENERS
// ----------------------------
searchBtn.addEventListener("click", () => {
    const query = searchInput.value.trim();
    if (query !== "") searchMovies(query);
});

searchInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") searchBtn.click();
});

// Close modal
modalClose.addEventListener("click", () => {
    modal.style.display = "none";
});

// Close modal on clicking outside
window.addEventListener("click", (e) => {
    if (e.target === modal) modal.style.display = "none";
});