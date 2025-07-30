    async function login() {
      const username = document.getElementById("username").value;
      const password = document.getElementById("password").value;
      try {
        const res = await fetch("http://localhost:8000/api/token/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ username, password }),
        });
        const data = await res.json();
        if (res.ok) {
          localStorage.setItem("token", data.token);
          console.log("Token stocké :", data.token);
          window.location.href = "create_quiz.html";
        } else {
          document.getElementById("errorMessage").textContent = "Erreur : " + JSON.stringify(data);
        }
      } catch (error) {
        document.getElementById("errorMessage").textContent = "Erreur réseau : " + error.message;
      }
    }
  