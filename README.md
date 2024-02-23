# Listening Test Application

## Overview
This is a simple FastAPI application that allows users to take a listening test and submit their scores to a MongoDB database. The application includes the following features:

- A home page that welcomes users to the application
- A form to submit a new test taker's name and score
- A page to view all test taker scores
- A search function to find test takers by name or score

## Prerequisites
To run this application, you will need the following:

- Python 3.8 or higher
- FastAPI
- MongoDB
- MongoEngine

## Installation
1. Clone the repository to your local machine.
2. Install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```
3. Start your MongoDB server.
4. Run the application using uvicorn:
    ```bash
    uvicorn main:app --reload
    ```

## Usage
1. Access the home page at http://localhost:8000/.
2. Fill out the form with your name and score, and submit the form.
3. View all test taker scores at http://localhost:8000/score.
4. Search for test takers by name using the `/search-name` endpoint.
5. Search for test takers by score using the `/search-score` endpoint.

## API Documentation
The API documentation is available at http://localhost:8000/docs.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
