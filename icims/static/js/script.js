function openModal() {
    document.getElementById('loginModal').style.display = 'block';
}

window.onclick = function(event) {
    if (event.target == document.getElementById('loginModal')) {
        document.getElementById('loginModal').style.display = 'none';
    }
}

function signIn() {
    // Handle sign in logic here
    alert('Sign in functionality would be implemented here');
}
