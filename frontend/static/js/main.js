async function sendMessage() {
    const userMessage = document.getElementById('userMessage').value;
    const response = await fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_message: userMessage }),
    });
    const data = await response.json();
    document.getElementById('messageResponse').textContent = data.response;
}

async function showMeHow() {
    const userInput = document.getElementById('showMeHowInput').value;
    const response = await fetch('/show_me_how', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_message: userInput }),
    });
    const data = await response.json();
    document.getElementById('showMeHowResponse').textContent = data.response;
}

async function uploadAudio() {
    const fileInput = document.getElementById('audioFile');
    const file = fileInput.files[0];
    if (!file) {
        alert('Please select a file first!');
        return;
    }
    const formData = new FormData();
    formData.append('audio_file', file);
    
    const response = await fetch('/upload_audio', {
        method: 'POST',
        body: formData,
    });
    const data = await response.json();
    document.getElementById('audioResponse').textContent = data.analysis;
}