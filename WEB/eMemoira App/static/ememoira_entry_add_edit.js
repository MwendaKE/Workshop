document.getElementById("refdate").addEventListener("input", (event) => {
    let dateref = event.target.value;
    if (/^\d{2}$/.test(dateref) || /^\d{2}-\d{2}$/.test(dateref)) {
        event.target.value = dateref + '-';
    }
});

// FORM VALIDATION

// Title Validation
document.getElementById("memoir-addentry-title-input").addEventListener("input", function () {
    let title = this.value.trim();
    let feedback = document.getElementById("title-entry-feedback");

    if (title.length > 5 && title.length <= 100) {
        feedback.textContent = "Memoir title is okay.";
        feedback.className = "entry-valid";
    } else {
        feedback.textContent = "Title must have more than 5 and less than 100 characters.";
        feedback.className = "entry-error";
    }
});

// Body Validation
document.getElementById("memoir-addentry-markdown-editor").addEventListener("input", function () {
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
document.getElementById("refdate").addEventListener("input", function () {
    let datevalue = this.value;  // Changed to 'this.value' for consistency
    let feedback = document.getElementById("date-entry-feedback");
    const pattern = /^\d{2}-\d{2}-\d{4}$/;

    if (pattern.test(datevalue)) {
        feedback.textContent = "Date is okay.";
        feedback.className = "entry-valid";
    } else {
        feedback.textContent = "Date must have a format 'dd-mm-yyyy'.";
        feedback.className = "entry-error";
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
    autoDownloadFontAwesome: false,
    toolbar: ["bold", "italic", "heading", "|", "quote"],
    status: false,
    class: "custom-simplemde"
});

// Ensure synchronization of SimpleMDE content on form submission in add-memoir-form.
// This is to see if the form is going to submit after submit button is pressed. However it does not solve the issue. So I have commented it out too.
// This is not needed in edit-memoir-form. In it, it submits successfully

document.getElementById("add-memoir-form").addEventListener("submit", function(event) {
    simplemde.codemirror.save(); // This ensures the content is in the textarea
});
*/


// ###### SIMPLE MDE INTEGRATION IN EDIT FORM //
// --------------------------------------------

/*
var simplemde = new SimpleMDE({
    element: document.getElementById("memoir-editentry-markdown-editor"),
    autoDownloadFontAwesome: false,
    toolbar: ["bold", "italic", "heading", "|", "quote"],
    status: false,
    class: "custom-simplemde" // Add custom class
});
*/

// I DECIDED TO REMOVED THE SIMPLEMDE EDITOR IN ALL <textarea>. But markups can still be used
// and rendered because the marked.js script is still there and working.


