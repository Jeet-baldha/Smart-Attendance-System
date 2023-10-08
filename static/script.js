// static/script.js
$(document).ready(function () {
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    const captureButton = document.getElementById('capture');
    const resultDiv = document.getElementById('result');

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
            console.log("video loaded");
        })
        .catch(function (error) {
            console.error('Error accessing the webcam:', error);
        });

    captureButton.addEventListener('click', function () {
        // Create a FormData object to send the image as a file attachment
        const formData = new FormData();
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        context.drawImage(video, 0, 0, 600, 450);

        // Convert canvas content to a Blob object
        canvas.toBlob(function (blob) {
            // Append the Blob as a file in the FormData object
            formData.append('image', blob, 'capture.jpg');

            // Send the FormData object with the image file to the server
            $.ajax({
                type: 'POST',
                url: '/recognize',
                data: formData,
                processData: false,
                contentType: false,
                success: function (response) {
                    // console.log('Response from server:', response);
                    response.recognized_names.forEach(element => {
                        console.log(element)
                    });
                    if (response.face_location) {
                        console.log('Face Location:', response.face_location);
                    } else {
                        console.log('Face Location not found in response.');
                    }
                },
                error: function (error) {
                    console.error('Error recognizing face:', error);
                }
            });
        }, 'image/jpeg');
    });
});
