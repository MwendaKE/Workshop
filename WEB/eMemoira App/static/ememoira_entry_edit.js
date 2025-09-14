document.addEventListener("DOMContentLoaded", (event) => {
    document.querySelectorAll("span").forEach(elem => {
        elem.textContent = "";
        elem.className = "entry-valid";
    });
    
    document.querySelectorAll("input").forEach(elem => {
        elem.style.color = "green";
    });
    
    document.querySelectorAll("textarea").forEach(elem => {
        elem.style.color = "green";
    });
});


//// DELETE MEMOIR ENTRY ///

function deleteMemoir(memoirId) {
    if (confirm("Are you sure to delete this memoir?")) {
        fetch(`/memoirs/${memoirId}/delete`, {
            method: "DELETE",
        })
        .then(response => {
            if (response.ok) {
                alert("Memoir deleted");
                const homeUrl = document.getElementById("body").getAttribute("data-home-url");
                window.location.href = homeUrl;
                
            } else {
                return response.json().then(data => {
                    alert("Error: " + data.message);
                });
            }
        })
        .catch(error => {
            alert(`Error Fetching data: ${error}`);
        });
    }
}

// FORM VALIDATION

// Title Validation
document.getElementById("memoir-editentry-title-input").addEventListener("input", function () {
    let title = this.value.trim();
    let feedback = document.getElementById("title-entry-feedback");

    if (title.length > 5 && title.length <= 100) {
        feedback.textContent = "Memoir title is okay.";
        feedback.className = "entry-valid";
        this.style.color = "green";
    } else {
        feedback.textContent = "Title must have more than 5 and less than 100 characters.";
        feedback.className = "entry-error";
        this.style.color = "red";
    }
});

// Body Validation
document.getElementById("memoir-editentry-markdown-editor").addEventListener("input", function () {
    let body = this.value.trim();
    let feedback = document.getElementById("body-entry-feedback");

    if (body.length >= 50) {
        feedback.textContent = "Memoir body is okay.";
        feedback.className = "entry-valid";
    } else {
        feedback.textContent = "Body must have more than 50 characters.";
        feedback.className = "entry-error";
    }
});

// Reference Date Validation

document.getElementById("refdate").addEventListener("input", function (event) {
    let datevalue = this.value;  // Changed to 'this.value' for consistency
    let feedback = document.getElementById("date-entry-feedback");
    
    if (datevalue.trim() === "") {
        feedback.textContent = "Date must have a format 'dd/mm/yyyy'.";
        feedback.className = "entry-error";
    } else {
        feedback.textContent = "Date is okay.";
        feedback.className = "entry-valid";
    }
});

// Form Submission Validation
document.getElementById("edit-memoir-form").addEventListener("submit", function(event) {
    let formIsValid = true;  // Reset 'formIsValid' at the start of each form submission

    // Check title validity
    let titleFeedback = document.getElementById("title-entry-feedback");
    if (titleFeedback.className === "entry-error") {
        formIsValid = false;
    }

    // Check body validity
    let bodyFeedback = document.getElementById("body-entry-feedback");
    if (bodyFeedback.className === "entry-error") {
        formIsValid = false;
    }

    // Check date validity
    let dateFeedback = document.getElementById("date-entry-feedback");
    if (dateFeedback.className === "entry-error") {
        formIsValid = false;
    }

    if (!formIsValid) {
        event.preventDefault();  // Prevent form submission if invalid
    }
});

// ###### SIMPLE MDE INTEGRATION IN EDIT FORM //
// --------------------------------------------
/*
var simplemde = new SimpleMDE({
    element: document.getElementById("memoir-editentry-markdown-editor"),
});

// Ensure synchronization of SimpleMDE content on form submission in add-memoir-form.
// This is to see if the form is going to submit after submit button is pressed. However it does not solve the issue. So I have commented it out too.
// This is not needed in edit-memoir-form. In it, it submits successfully

document.getElementById("add-memoir-form").addEventListener("submit", function(event) {
    simplemde.codemirror.save(); // This ensures the content is in the textarea
});
*/

