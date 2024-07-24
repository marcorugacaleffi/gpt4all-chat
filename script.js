document.getElementById('user-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendPrompt();
    }
});

function sendPrompt() {
    const userInput = document.getElementById('user-input').value;
    const chatMessages = document.getElementById('chat-messages');

    if (userInput.trim() === '') return;

    const userMessage = document.createElement('div');
    userMessage.className = 'user-message';
    userMessage.textContent = userInput;
    chatMessages.appendChild(userMessage);

    fetch('https://192.168.208.6:4891/chat', {  // Assicurati che l'indirizzo IP e la porta siano corretti
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: userInput })
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = document.createElement('div');
        botMessage.className = 'bot-message';
        botMessage.textContent = data.response;
        chatMessages.appendChild(botMessage);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    })
    .catch(error => console.error('Error:', error));

    document.getElementById('user-input').value = '';
}
