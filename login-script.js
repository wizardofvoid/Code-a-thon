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


// Select the form box
const box = document.querySelector('.box');

// Add mousemove event listener for tilt effect
box.addEventListener('mousemove', function (e) {
    const boxWidth = box.offsetWidth;
    const boxHeight = box.offsetHeight;
    const centerX = box.offsetLeft + boxWidth / 2;
    const centerY = box.offsetTop + boxHeight / 2;
    const mouseX = e.clientX - centerX;
    const mouseY = e.clientY - centerY;

    const rotateX = (mouseY / boxHeight) * -10; // Adjusts tilt based on mouse Y position
    const rotateY = (mouseX / boxWidth) * 10; // Adjusts tilt based on mouse X position

    box.style.transform = `rotateY(${rotateY}deg) rotateX(${rotateX}deg)`;
});

// Reset the tilt effect when the mouse leaves the box
box.addEventListener('mouseleave', function () {
    box.style.transform = `rotateY(0deg) rotateX(0deg)`;
});
