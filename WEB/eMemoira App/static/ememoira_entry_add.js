// FORM VALIDATION

// Title Validation
document.getElementById("memoir-addentry-title-input").addEventListener("input", function () {
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
document.getElementById("memoir-addentry-markdown-editor").addEventListener("input", function () {
    let body = this.value.trim();
    let feedback = document.getElementById("body-entry-feedback");

    if (body.length >= 50) {
        feedback.textContent = "Memoir body is okay.";
        feedback.className = "entry-valid";
        this.style.color = "green";
    } else {
        feedback.textContent = "Body must have more than 50 characters.";
        feedback.className = "entry-error";
        this.style.color = "red";
    }
});

// Reference Date Validation

document.getElementById("refdate").addEventListener("input", function (event) {
    let datevalue = this.value;  // Changed to 'this.value' for consistency
    let feedback = document.getElementById("date-entry-feedback");
    
    if (datevalue.trim() === "") {
        feedback.textContent = "Date must have a format 'dd/mm/yyyy'.";
        feedback.className = "entry-error";
        this.style.color = "red";
    } else {
        feedback.textContent = "Date is okay.";
        feedback.className = "entry-valid";
        this.style.color = "green";
    }
});

// Form Submission Validation
document.getElementById("add-memoir-form").addEventListener("submit", function(event) {
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


// ###### SIMPLE MDE INTEGRATION IN ADD FORM //
// --------------------------------------------

// The code below fails to work. As in it works but the form does not submit.
// I have commented it out to allow form submission

/*
var simplemde = new SimpleMDE({
    element: document.getElementById("memoir-addentry-markdown-editor"),
});
*/
