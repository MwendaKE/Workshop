import { useState } from "react";
import "./App.css";

function App() {
  const [keyword, setKeyword] = useState("");
  const [articles, setArticles] = useState([]);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);

  const API_KEY = "e40e33cd336244b2b45a5d87dca23b58"; // Replace with your key
  const PAGE_SIZE = 10; // Articles per page

  const searchNews = async (newSearch = true) => {
    if (keyword.trim() === "") return;

    setLoading(true);

    // If new search, reset page to 1
    const currentPage = newSearch ? 1 : page;

    try {
      const res = await fetch(
        `https://newsapi.org/v2/everything?q=${encodeURIComponent(
          keyword
        )}&pageSize=${PAGE_SIZE}&page=${currentPage}&sortBy=publishedAt&language=en&apiKey=${API_KEY}`
      );
      const data = await res.json();

      if (data.status === "ok") {
        if (newSearch) {
          setArticles(data.articles);
          setPage(2); // next page
        } else {
          setArticles((prev) => [...prev, ...data.articles]);
          setPage((prev) => prev + 1);
        }
      } else {
        alert("No news found");
      }
    } catch (err) {
      console.error(err);
      alert("Error fetching news");
    }

    setLoading(false);
  };

  return (
    <div className="app-container">
      <div className="news-box">
        <h2>📰 News Search App</h2>

        <input
          type="text"
          placeholder="Enter keyword..."
          value={keyword}
          onChange={(e) => setKeyword(e.target.value)}
        />

        <button onClick={() => searchNews(true)}>Search</button>

        {loading && <p className="loading">Loading...</p>}

        <div className="articles">
          {articles.map((article, idx) => (
            <div className="article-card" key={idx}>
              {article.urlToImage && (
                <img src={article.urlToImage} alt="news" />
              )}
              <h3>{article.title}</h3>
              <p>{article.description}</p>
              <a href={article.url} target="_blank" rel="noopener noreferrer">
                Read more
              </a>
            </div>
          ))}
        </div>

        {/* Load More Button */}
        {articles.length >= PAGE_SIZE && (
          <button
            className="load-more"
            onClick={() => searchNews(false)}
            disabled={loading}
          >
            Load More
          </button>
        )}
      </div>
    </div>
  );
}

export default App;

