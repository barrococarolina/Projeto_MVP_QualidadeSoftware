document.getElementById("predict-form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const dados = {
        school: document.getElementById("school").value,
        sex: document.getElementById("sex").value,
        age: parseInt(document.getElementById("age").value),
        G1: parseInt(document.getElementById("G1").value),
        G2: parseInt(document.getElementById("G2").value),
        subject: document.getElementById("subject").value
    };

    const resposta = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dados)
    });

    const resultado = await resposta.json();
    document.getElementById("resultado").innerText = 
        resposta.ok ? `Nota prevista (G3): ${resultado.predicted_G3}` : `Erro: ${resultado.mensagem}`;
});