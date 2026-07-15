const sendBtn = document.getElementById("send-btn");

const userInput = document.getElementById("user-input");

const chatBox = document.getElementById("chat-box");


function addMessage(text, sender) {

    const message = document.createElement("div");

    message.classList.add("message");

    message.classList.add(sender);

    const title = document.createElement("strong");

    title.textContent = sender === "user"
        ? "👤 You"
        : "🤖 SOC AI";

    const body = document.createElement("p");

    body.textContent = text;

    message.appendChild(title);

    message.appendChild(body);

    chatBox.appendChild(message);

    chatBox.scrollTop = chatBox.scrollHeight;

    return message;

}


async function sendMessage() {

    const question = userInput.value.trim();

    if (!question) {

        return;

    }

    const welcome = document.querySelector(".welcome");

    if (welcome) {

        welcome.remove();

    }

    addMessage(question, "user");

    userInput.value = "";

    const thinking = addMessage("Thinking...", "ai");

    try {

        const response = await fetch("http://127.0.0.1:8001/chat", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                question: question

            })

        });

        const data = await response.json();

        thinking.remove();

        addMessage(data.answer, "ai");

    }

    catch (error) {

        thinking.remove();

        addMessage("Unable to connect to the backend.", "ai");

        console.error(error);

    }

}


sendBtn.addEventListener("click", sendMessage);


userInput.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {

        sendMessage();

    }

});