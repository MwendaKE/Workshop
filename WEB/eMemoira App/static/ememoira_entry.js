function displayMemoirEntry(memoirId) {
    fetch(`/api/memoirs/${memoirId}`)
    .then(response => response.json())
    .then(data => {
        const entryTitle = document.getElementById("memoir-entry-title");
        const entryTime = document.getElementById("memoir-entry-time");
        const referTime = document.getElementById("memoir-refer-time");
        const entryBody = document.getElementById("memoir-entry-container");
        
        entryTitle.innerText = data.title;
        entryTime.innerText = `Created: ${data.date_created}`;
        referTime.innerText = `Reference: ${data.date_of_reference}`;
        entryBody.innerHTML = marked.parse(data.body);
        
        const picsContainer = document.getElementById("memoir-pics-container");
        const audsContainer = document.getElementById("memoir-auds-container");
        const vidsContainer = document.getElementById("memoir-vids-container");
        
        picsContainer.innerHTML = "";
        
        const memoirPics = data.pictures;
        const memoirAuds = data.audios;
        const memoirVids = data.videos;
        
        // PICTURES
        
        if (memoirPics.length > 0) {
            memoirPics.forEach(imageUrl => {
                const linkElem = document.createElement("a"); // *
                linkElem.href = `/${imageUrl}`;
                linkElem.setAttribute("data-fancybox", "memoir-images");
                linkElem.setAttribute("data-caption", `Picture related to ${data.title}`);
                
                const imageElem = document.createElement("img");
                imageElem.src = `/${imageUrl}`; // Set the image URL
                imageElem.alt = "Image";
                
                linkElem.appendChild(imageElem); // *
                picsContainer.appendChild(linkElem); // * replace with imageElem 
            });
            
        } else {
            picsContainer.innerHTML = "No images available";
        }
        
        // AUDIOS
        
        if (memoirAuds.length > 0) {
            memoirAuds.forEach(audioUrl => {
                const audioElem = document.createElement("audio");
                audioElem.controls = true;
                
                sourceElem = document.createElement("source");
                sourceElem.src = `/${audioUrl}`; // Set the URL
                sourceElem.type = "audio/mpeg";
                
                audioElem.appendChild(sourceElem);
                audsContainer.appendChild(audioElem);
            });
        } else {
            audsContainer.innerHTML = "No audios available";
        }
        
        // VIDEO
        
        if (memoirVids.length > 0) {
            memoirVids.forEach(videoUrl => {
                const videoCardElem = document.createElement("div"); // *
                
                const videoElem = document.createElement("video");
                videoElem.controls = true;
                
                sourceElem = document.createElement("source");
                sourceElem.src = `/${videoUrl}`; // Set the URL
                sourceElem.type = "video/mp4";
                
                videoElem.appendChild(sourceElem);
                videoCardElem.appendChild(videoElem);
                vidsContainer.appendChild(videoCardElem);
            });
        } else {
            vidsContainer.innerHTML = "No videos available";
        }
    })
    .catch(error => {
        alert(error);
    });
}

// AUTOPLAY AND PAUSE VIDEOS

const videos = document.querySelectorAll("video");

videos.forEach(video => {
    video.addEventListener('mouseover', () => {
        video.play();
    });
    
    video.addEventListener('mouseleave', () => {
        video.pause();
    });
});