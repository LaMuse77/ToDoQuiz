    async function register() {
      const username = document.getElementById('regUsername').value;
      const email = document.getElementById('regEmail').value;
      const password = document.getElementById('regPassword').value;
      const role = document.getElementById('regRole').value;

      const res = await fetch(`${baseUrl}/api/accounts/register/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, email, password, role })
      });

      const data = await res.json();

      if (res.ok) {
        alert('Inscription réussie ! Token : ' + data.token);
        localStorage.setItem("token", data.token);
        toggleToLogin(); // on retourne au login
      } else {
        alert('Erreur : ' + JSON.stringify(data));
      }
    }
    