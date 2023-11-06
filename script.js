document.addEventListener('DOMContentLoaded', function() {
    const messagesContainer = document.getElementById('messages');
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');
    const localVideo = document.getElementById('localVideo');
    const remoteVideo = document.getElementById('remoteVideo');
    const startCallButton = document.getElementById('startCallButton');
    const joinCallButton = document.getElementById('joinCallButton');

    let localStream;
    let remoteStream;

    sendButton.addEventListener('click', function() {
        const message = messageInput.value;
        if (message.trim() !== '') {
            const messageElement = document.createElement('div');
            messageElement.textContent = message;
            messagesContainer.appendChild(messageElement);
            messageInput.value = '';
        }
    });

    messageInput.addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            sendButton.click();
        }
    });

    startCallButton.addEventListener('click', startCall);
    joinCallButton.addEventListener('click', joinCall);

    function startCall() {
        navigator.mediaDevices.getUserMedia({ video: false, audio: true })
            .then((stream) => {
                localStream = stream;
                localVideo.srcObject = stream;
            })
            .catch((error) => {
                console.error('Error accessing microphone:', error);
            });

        
    }

    function joinCall(offer) {
        navigator.mediaDevices.getUserMedia({ video: false, audio: true })
            .then((stream) => {
                localStream = stream;
                localVideo.srcObject = stream;
            })
            .catch((error) => {
                console.error('Error accessing microphone:', error);
            });

       
    }
});
