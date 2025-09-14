// Execute on document load

document.addEventListener("DOMContentLoaded", (event) => {
    fetchAndDisplayMemoirs();
});

function fetchAndDisplayMemoirs() {
    fetch('/api/memoirs')
        .then(response =>  {
            if (!response.ok) {
                throw new Error("Failed to fetch memoirs: " + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            const memoirsContainer = document.getElementById("memoirs-container");
            memoirsContainer.innerHTML = ""; 
            
            if (data && data.length > 0) {
                data.forEach(memoir => {
                    const memoirDiv = document.createElement("div");
                    memoirDiv.classList.add("memoir-item");
        
                    //----------
                    const mTitle = document.createElement("h5");
                    const mTitleLink = document.createElement("a");
                    const mBody = document.createElement("p");
                    const mDate = document.createElement("small");
                    
                    mTitleLink.href = `/memoirs/${memoir.id}`;
                    mTitleLink.innerText = memoir.title;
                    
                    mTitle.appendChild(mTitleLink);
                    
                    mBody.innerHTML = marked.parse(memoir.body);
                    mBody.style.textAlign = "justify";
                    mDate.textContent = `Created: ${memoir.date_created}  |  Reference: ${memoir.date_of_reference}`;
                    
                    memoirDiv.appendChild(mTitle);
                    memoirDiv.appendChild(mBody);
                    memoirDiv.appendChild(mDate);
        
                    memoirsContainer.appendChild(memoirDiv);
                });
            } else {
                memoirsContainer.innerHTML = "<p>No memoirs yet. Click the button above to add memoirs.</p>"
            }
        })
        .catch (error => {
            alert(error);
        });    
}
