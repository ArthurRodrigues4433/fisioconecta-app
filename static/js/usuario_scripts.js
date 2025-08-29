document.getElementById("LoginForm").addEventListener("submit", async function (e) {
    e.preventDefault(); // evita reload da página

    const data = {
            nome: document.getElementById("nome").value,
            crefito: document.getElementById("crefito").value,
            email: document.getElementById("email").value,
            senha: document.getElementById("senha").value,
            telefone: document.getElementById("telefone").value,
            especialidade: document.getElementById("especialidade").value,
            cidade: document.getElementById("cidade").value,
            endereco: document.getElementById("endereco").value,
            estado: document.getElementById("estado").value,
            status: true,
            admin: false
        };

    try {
        const response = await fetch("http://127.0.0.1:8000/auth/criar_conta_fisio", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById("resposta").style.color = "green";
            document.getElementById("resposta").innerText = "✅ Cadastro realizado com sucesso!";
            
            localStorage.setItem("token", result.access_token);

            setTimeout(() => {
                window.location.href = "/";
            }, 1000);
        } else {
            document.getElementById("resposta").style.color = "red";
            document.getElementById("resposta").innerText = result.detail;
        }
    } catch (error) {
        document.getElementById("resposta").style.color = "red";
        document.getElementById("resposta").innerText = "Erro no servidor.";
        console.error("Erro:", error);
    }
});