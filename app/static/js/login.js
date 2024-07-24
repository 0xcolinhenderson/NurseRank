const login_form = document.getElementById('login_form');

function login(e) {
    e.preventDefault();
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    fetch("/api/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        credentials: "same-origin",
        body: JSON.stringify({ email: email, password: password }),
    })
    .then((res) => {
        if (!res.ok) {
            throw new Error('Network response was not ok');
        }
        return res.json();
    })
    .then((data) => {
        console.log(data);
        // Redirect to the home page after successful login
        if (data.redirect) {
            window.location.href = data.redirect;
        } else {
            // Optionally handle cases where no redirect URL is provided
            console.error('No redirect URL provided');
        }
    })
    .catch((err) => {
        console.log(err);
    });
}

login_form.addEventListener('submit', login);
