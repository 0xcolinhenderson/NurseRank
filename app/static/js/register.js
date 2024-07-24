const register_form = document.getElementById('register_form');

function register(e) {
    e.preventDefault();
    let firstname = document.getElementById('firstname').value;
    let lastname = document.getElementById('lastname').value;
    let email = document.getElementById('email').value;
    let password = document.getElementById('password').value;
    let password2 = document.getElementById('password2').value;

    fetch("/api/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        credentials: "same-origin",
        body: JSON.stringify({ firstname: firstname, lastname: lastname, email: email, password: password, password2: password2 }),
    })
    .then((res) => {
        if (!res.ok) {
            throw new Error('Network response was not ok');
        }
        return res.json();
    })
    .then((data) => {
        console.log(data);
        if (data.redirect) {
            window.location.href = data.redirect;  // Redirect to the provided URL
        } else {
            // Handle cases where no redirect URL is provided
            console.error('No redirect URL provided');
        }
        register_form.reset();
    })
    .catch((err) => {
        console.log(err);
    });
}

register_form.addEventListener('submit', register);
