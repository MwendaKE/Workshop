// Get form and button elements
const form = document.getElementById('applicationForm');
const submitButton = form.querySelector('button[type="submit"]');
const messageDiv = document.getElementById('message');

// Validation functions
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function isValidPhone(phone) {
    const digitsOnly = phone.replace(/\D/g, '');
    return digitsOnly.length >= 10;
}

function validateField(input) {
    const value = input.value.trim();
    let isValid = true;
    let errorMessage = '';
    
    // Remove any existing styling first
    input.style.borderColor = '';
    
    // Check if field is empty
    if (!value) {
        isValid = false;
        if (input.tagName === 'SELECT') {
            errorMessage = 'Please select a position';
        } else {
            errorMessage = 'This field is required';
        }
        input.style.borderColor = 'red';
        return { isValid, message: errorMessage };
    }
    
    // Special validation for select field (position)
    if (input.tagName === 'SELECT') {
        if (value === "") {
            isValid = false;
            errorMessage = 'Please select a position';
            input.style.borderColor = 'red';
        } else {
            isValid = true;
            input.style.borderColor = 'green';
        }
        return { isValid, message: errorMessage };
    }
    
    // Email validation
    if (input.type === 'email') {
        if (!isValidEmail(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid email address';
            input.style.borderColor = 'red';
        } else {
            isValid = true;
            input.style.borderColor = 'green';
        }
    }
    
    // Phone validation
    if (input.name === 'phone') {
        if (!isValidPhone(value)) {
            isValid = false;
            errorMessage = 'Phone number must be at least 10 digits';
            input.style.borderColor = 'red';
        } else {
            isValid = true;
            input.style.borderColor = 'green';
        }
    }
    
    // For other valid fields (text, textarea)
    if (isValid && input.type !== 'email' && input.name !== 'phone' && input.tagName !== 'SELECT') {
        input.style.borderColor = 'green';
    }
    
    return { isValid, message: errorMessage };
}

// Function to check if all fields are filled and valid
function checkFormValidity() {
    const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
    let allFilled = true;
    let allValid = true;
    
    // Clear previous error messages
    document.querySelectorAll('.error-message').forEach(msg => msg.remove());
    
    inputs.forEach(input => {
        const validation = validateField(input);
        
        if (!input.value.trim()) {
            allFilled = false;
            input.style.borderColor = ''; // Reset border if empty
        } else if (!validation.isValid) {
            allValid = false;
            // Show error message
            const errorMsg = document.createElement('div');
            errorMsg.className = 'error-message';
            errorMsg.style.color = 'red';
            errorMsg.style.fontSize = '12px';
            errorMsg.style.marginTop = '-5px';
            errorMsg.style.marginBottom = '10px';
            errorMsg.textContent = validation.message;
            input.parentNode.insertBefore(errorMsg, input.nextSibling);
        } else {
            // Field is valid - green border
            input.style.borderColor = 'green';
        }
    });
    
    // Enable/disable submit button
    submitButton.disabled = !allFilled || !allValid;
}

// Add event listeners to all form inputs including select
form.querySelectorAll('input, textarea, select').forEach(input => {
    input.addEventListener('input', function() {
        checkFormValidity();
    });
    
    input.addEventListener('change', function() {
        checkFormValidity();
    });
    
    // Also validate on blur (when user leaves the field)
    input.addEventListener('blur', checkFormValidity);
});

// Handle form submission
form.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Final validation before submission
    checkFormValidity();
    if (submitButton.disabled) return;
    
    // Disable button during submission
    submitButton.disabled = true;
    submitButton.textContent = 'Submitting...';
    
    const formData = new FormData(this);
    const data = {
        full_name: formData.get('full_name'),
        phone: formData.get('phone'),
        email: formData.get('email'),
        position: formData.get('position'),
        experience: formData.get('experience')
    };
    
    fetch('/submit', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        messageDiv.innerHTML = '<p style="color: green;">Application Submitted Successfully!</p>';
        
        // Reset borders after successful submission
        form.querySelectorAll('input, textarea, select').forEach(input => {
            input.style.borderColor = '';
        });
        
        form.reset();
        checkFormValidity();
    })
    .catch(error => {
        messageDiv.innerHTML = '<p style="color: red;">Error submitting application</p>';
        checkFormValidity();
    })
    .finally(() => {
        submitButton.textContent = 'Submit Application';
    });
});

// Initial check when page loads
checkFormValidity();