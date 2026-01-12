// ----------------------------
// API SETTINGS
// ----------------------------
// Spoonacular has a free recipe API. We'll use a demo endpoint.
const apiKey = "24ed44a158d842dskjdjjdj83837f2c0c4d2f71"; // Replace with your key
const apiURL = "https://api.spoonacular.com/recipes/complexSearch";

// DOM ELEMENTS
const searchInput = document.getElementById("searchInput");
const cuisineSelect = document.getElementById("cuisineSelect");
const recipesContainer = document.getElementById("recipesContainer");

// FAVORITES (from localStorage)
let favorites = JSON.parse(localStorage.getItem("favorites")) || [];

// ----------------------------
// FETCH RECIPES
// ----------------------------
async function fetchRecipes(query="", cuisine="") {
    try {
        const url = `${apiURL}?apiKey=${apiKey}&query=${query}&cuisine=${cuisine}&number=10`;
        const res = await fetch(url);
        const data = await res.json();

        displayRecipes(data.results || []);
    } catch (error) {
        console.error("Error fetching recipes:", error);
        recipesContainer.innerHTML = "<p>Failed to load recipes.</p>";
    }
}

// ----------------------------
// DISPLAY RECIPES
// ----------------------------
function displayRecipes(recipes) {
    recipesContainer.innerHTML = "";
    recipes.forEach(recipe => {
        const div = document.createElement("div");
        div.classList.add("recipe-card");
        div.innerHTML = `
            <img src="${recipe.image}" alt="${recipe.title}">
            <h3>${recipe.title}</h3>
            <button class="fav-btn" onclick="toggleFavorite(${recipe.id}, '${recipe.title}', '${recipe.image}')">
                ${favorites.some(f => f.id === recipe.id) ? "Remove from Favorites" : "Add to Favorites"}
            </button>
        `;
        recipesContainer.appendChild(div);
    });
}

// ----------------------------
// FAVORITE TOGGLE
// ----------------------------
function toggleFavorite(id, title, image) {
    const index = favorites.findIndex(f => f.id === id);
    if(index > -1){
        favorites.splice(index, 1);
    } else {
        favorites.push({id, title, image});
    }
    localStorage.setItem("favorites", JSON.stringify(favorites));
    fetchRecipes(searchInput.value, cuisineSelect.value); // refresh buttons
}

// ----------------------------
// EVENT LISTENERS
// ----------------------------
searchInput.addEventListener("input", () => fetchRecipes(searchInput.value, cuisineSelect.value));
cuisineSelect.addEventListener("change", () => fetchRecipes(searchInput.value, cuisineSelect.value));

// ----------------------------
// INITIAL LOAD
// ----------------------------
fetchRecipes();
