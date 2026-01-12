from flask import Flask, render_template, request, redirect, jsonify
import requests

NEWSAPI = "e40e33cd336244b2b45a5d87dca2id62&b58"
NEWSURL = "https://newsapi.org/v2/everything"


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    
    
@app.route('/search')
def search():
    search_query = request.args.get('q')
    
    if not search_query:
        return jsonify({"error": "Sorry, nothing to search."}), 400
        
    params = {
        "q": search_query,
        "apiKey": NEWSAPI,
        "language": "en", # Optional
        "sortBy": "relevancy" # Optional: Sort by popularity or publishedAt
    }
    
    response = requests.get(NEWSURL, params=params) 
    
    if response.status_code == 200:
        return jsonify(response.json())
        
    return jsonify({"error": "Searching news API failed."}), response.status_code
    
if __name__ == "__main__":
    app.run(debug=True)
