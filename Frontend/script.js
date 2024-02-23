function calculateScore() {
    const optionScores = {
        "Not at All": 1,
        "Rarely": 2,
        "Sometimes": 3,
        "Often": 4,
        "Very Often": 5
    };

    const radioButtons = document.querySelectorAll('#questions-form input[type="radio"]:checked');
    let netScore = 0;

    radioButtons.forEach(radioButton => {
        netScore += optionScores[radioButton.value];
    });

    const userName = document.getElementById("user-name").textContent;

    // Prepare the data to be sent to the backend
    const postData = {
        name: userName,
        score: netScore
    };

    // Make a POST request to the /score endpoint
    fetch('http://localhost:3001/score', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(postData),
    })
        .then(response => response.json())
        .then(data => {
            alert(`Your net score is: ${netScore}\n\nServer response:\n${JSON.stringify(data)}`);
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while sending the score to the server.');
        });
}

document.getElementById("start-form").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission
    const userName = document.getElementById("fullname").value;
    document.getElementById("user-name").textContent = userName;
    document.getElementById("fullname").disabled = true;

    document.getElementById("questions-form").style.display = "block";
    document.getElementById("final-submit-button").style.display = "block";

    console.log("userName:", userName);
    console.log("user-name element:", document.getElementById("user-name"));
});

document.getElementById("questions-form").addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission
    calculateScore();
});
