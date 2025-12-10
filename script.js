function sendMessage() {
    let input = document.getElementById("userInput");
    let message = input.value;

    // Tambahkan pesan user ke chatbox
    document.getElementById("chatbox").innerHTML += `
        <div class="user">${message}</div>
    `;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("chatbox").innerHTML += `
            <div class="bot">${data.reply}</div>
        `;
    });

    input.value = "";
}
