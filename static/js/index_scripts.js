document.getElementById("loginForm").addEventListener("submit", async function (e) {
    e.preventDefault(); // evita reload da página

    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;

    try {
        const response = await fetch("http://127.0.0.1:8000/auth/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email: email, senha: senha })
        });

        const data = await response.json();

        if (response.ok) {
            document.getElementById("resposta").style.color = "green";
            document.getElementById("resposta").innerText = "✅ Login realizado com sucesso!";
            
            // Armazena o token no localStorage
            localStorage.setItem("token", data.eccess_token);

            // Redireciona o usuário para outra página após login
            setTimeout(() => {
                window.location.href = "/dashboard_usuario"; // ajuste para a rota que você tiver
            }, 1000);

        } else {
            document.getElementById("resposta").style.color = "red";
            document.getElementById("resposta").innerText = data.detail;
        }
    } catch (error) {
        document.getElementById("resposta").style.color = "red";
        document.getElementById("resposta").innerText = "Erro no servidor.";
        console.error("Erro:", error);
    }
});

// botão "registrar usuário"
    document.getElementById("btnRegistrar").addEventListener("click", (e) => {
        e.preventDefault(); // evita comportamento padrão do <a>
        window.location.href = "http://127.0.0.1:8000/criar_usuario"; // ajuste para a rota real do seu backend
    });

    // botão "registrar fisioterapeuta"
    document.getElementById("btnRegistrarProf").addEventListener("click", (e) => {
        e.preventDefault();
        window.location.href = "http://127.0.0.1:8000/criar_fisio"; 
    });