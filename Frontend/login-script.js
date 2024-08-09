// Get the form and error message element
const form = document.getElementById('loginForm');
const errorMessage = document.getElementById('error-message');

// Handle form submission
form.addEventListener('submit', function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simple validation
    if (!username || !password) {
        showError('Please fill in all fields.');
        return;
    }

    // Simulate successful login (replace this with actual login logic)
    alert('Login successful!');

    // Clear error message
    errorMessage.style.display = 'none';
});

// Show error message
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.style.display = 'block';
    errorMessage.style.opacity = 1;

    // Hide after 3 seconds
    setTimeout(() => {
        errorMessage.style.opacity = 0;
        setTimeout(() => {
            errorMessage.style.display = 'none';
        }, 500);
    }, 3000);
}

// Focus effect on inputs
document.querySelectorAll('.inputBox input').forEach(input => {
    input.addEventListener('focus', () => {
        input.classList.add('focused');
    });
    
    input.addEventListener('blur', () => {
        if (input.value === '') {
            input.classList.remove('focused');
        }
    });
});
