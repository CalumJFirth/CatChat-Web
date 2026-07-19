console.log("JavaScript is running!");

async function getMessages() {
    const response = await fetch("/messages")
    const messages = await response.json();

    const div = document.getElementById("messages");

    for (const message of messages) {

        const p = document.createElement("p");

        p.textContent = `${message.username}: ${message.text}`;

        div.appendChild(p);

}

}
    
    

}

getMessages();




