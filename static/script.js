console.log("JavaScript is running!");

async function getMessages() {
    const response = await fetch("/messages");
    const messages = await response.json();

    const div = document.getElementById("messages");
    div.replaceChildren();

    for (const message of messages) {

        const p = document.createElement("p");

        p.textContent = `${message.username}: ${message.text}`;

        div.appendChild(p);
    }

}   

async function sendMessage() {
    const input = document.getElementById("messageInput");
    if (input.value.trim() === "") {
    return;
    }
    const message = {
        username: "Calum",
        text: input.value
    };
    console.log("Sending message to server!")

    await fetch("/messages", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(message)
    });

    await getMessages();
    input.value = "";

    
}

const input = document.getElementById("messageInput");
input.onkeydown = function(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

};



// WebSockets
const socket = new WebSocket("ws://127.0.0.1:8765");

socket.onopen = () => {
    console.log("Connected");

    socket.send("Hello from the browser!");
};

socket.onmessage = (event) => {
    console.log(event.data);
}

socket.onclose = () => {
    console.log("Disconnected");
};



const button = document.getElementById("sendButton");
button.onclick = sendMessage

getMessages();
setInterval(getMessages, 1000);

