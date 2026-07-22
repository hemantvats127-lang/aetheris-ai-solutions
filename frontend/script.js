const API_URL = "http://127.0.0.1:5000/chat"; // Local test ke liye
let conversationHistory = [];

async function sendMessage() {
    const inputField = document.getElementById("userInput");
    const message = inputField.value.trim();
    if (!message) return;

    appendMessage(message, "user-message");
    inputField.value = "";

    conversationHistory.push({ role: "user", content: message });

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ messages: conversationHistory })
        });

        const data = await response.json();
        const aiReply = data.reply;

        appendMessage(aiReply, "ai-message");
        conversationHistory.push({ role: "assistant", content: aiReply });

    } catch (error) {
        console.error("Error:", error);
        appendMessage("Apologies, I am experiencing network issues. Please try again in a moment.", "ai-message");
    }
}

function appendMessage(text, className) {
    const chatBox = document.getElementById("chatBox");
    const msgDiv = document.createElement("div");
    msgDiv.classList.add("message", className);
    msgDiv.innerText = text;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function handleKeyPress(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
}
