const baseUrl = "http://localhost:8000";

// Function to get CSRF token from cookie
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const csrftoken = getCookie('csrftoken');

  try {
    const res = await fetch(`${baseUrl}/api/accounts/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({ username, password }),
      credentials: 'include', // Ensure cookies are sent
    });

    const text = await res.text();
    let data;
    try {
      data = JSON.parse(text);
    } catch {
      data = { message: text };
    }

    if (res.ok) {
      localStorage.setItem("token", data.access);
      localStorage.setItem("role", data.role);
      if (data.role === "participant") {
        window.location.href = "chooseCategorie.html";
      } else if (data.role === "organisateur") {
        window.location.href = "dashboard.html";
      } else {
        document.getElementById("errorMessage").textContent = "Rôle inconnu.";
      }
    } else {
      document.getElementById("errorMessage").textContent = "Erreur : " + JSON.stringify(data);
    }
  } catch (error) {
    document.getElementById("errorMessage").textContent = "Erreur réseau : " + error.message;
  }
}

async function register() {
  const username = document.getElementById('regUsername').value;
  const email = document.getElementById('regEmail').value;
  const password = document.getElementById('regPassword').value;
  const role = document.getElementById('regRole').value;
  const csrftoken = getCookie('csrftoken');

  try {
    const res = await fetch(`${baseUrl}/api/accounts/register/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({ username, email, password, role }),
      credentials: 'include',
    });

    const text = await res.text();
    let data;
    try {
      data = JSON.parse(text);
    } catch {
      data = { message: text };
    }

    if (res.ok) {
      localStorage.setItem("token", data.token);
      alert("Inscription réussie !");
      window.location.href = "login.html";
    } else {
      alert("Erreur : " + JSON.stringify(data));
    }
  } catch (error) {
    alert("Erreur réseau : " + error.message);
  }
}