const baseUrl = "http://localhost:8000" ;

async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch(`${baseUrl}/api/token/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password })
    });

    const text = await res.text();
    let data;
    try {
    data = JSON.parse(text);
    } catch {
    data = { message: text };
    }

    if (res.ok) {
      localStorage.setItem("token", data.access);  // ou data.token selon ton backend
      localStorage.setItem("role", data.role);     // stocke le rôle

      // Redirection selon le rôle
      if (data.role === "participant") {
        window.location.href = "choosecategorie.html";
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

  const res = await fetch(`${baseUrl}/api/accounts/register/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, email, password, role })
  });

  const data = await res.json();
  if (res.ok) {
    localStorage.setItem("token", data.token);
    alert("Inscription réussie !");
    window.location.href = "login.html";
  } else {
    alert("Erreur : " + JSON.stringify(data));
  }
}
