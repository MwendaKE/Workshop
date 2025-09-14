function searchAndDisplayNews() {
    const userInput = document.getElementById("search-query").value.trim();

    if (userInput) {
        fetch(`/search?q=${encodeURIComponent(userInput)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                const displayContainer = document.getElementById('display-area');
                displayContainer.innerHTML = "";

                if (data.articles && data.articles.length > 0) {
                    data.articles.forEach(article => {
                        const articleContainer = document.createElement("div");
                        articleContainer.classList.add("article-item");
                        
                        articleContainer.innerHTML = `<h5><a href="${article.url}" target="_blank">${article.title}</a></h5><p>${article.description}</p>
                                                      <small>Source: ${article.source.name} </small><span> | </span><small> Published At: ${article.publishedAt}</small>`;
                        displayContainer.appendChild(articleContainer);
                    });
                } else {
                    displayContainer.innerHTML = "<p>Sorry. No news articles found. Try searching for something else.</p>";
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                alert("An error occurred while fetching news articles. Please try again later.");
            });
    } else {
        alert("Please enter a search term.");
    }
}