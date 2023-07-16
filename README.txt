# Tiktoken Tokenizer Flask Application
This is a Flask application that uses OpenAI's tiktoken library to tokenize text.

## Files
- `flask_app.py`: The main Python application file.
- `swagger.yaml`: The Swagger definition for the API endpoint.
- `Procfile`: The file used for declaring what commands are run by your application's containers on the Deis platform.
- `Dockerfile`: The Dockerfile for building a Docker image of the application.
- `requirements.txt`: The file listing the Python dependencies that need to be installed.

## Running the Application
1. Install the Python dependencies by running `pip install -r requirements.txt`.
2. Run the Flask application by running `python flask_app.py`.

## Docker
To build a Docker image of the application, navigate to the directory containing the Dockerfile and run `docker build -t tiktoken_flask_app .`. You can then run the Docker image with `docker run -p 4000:80 tiktoken_flask_app`.

## Deployment
This application is ready to be deployed on a platform like Google Cloud Run. You will need to build a Docker image and push it to a container registry before you can deploy it. Refer to the platform's documentation for specific instructions.

## API Endpoint
The application has a single API endpoint (`/tokenize`) that accepts POST requests. The POST request should include a JSON body with two properties: `text` (the text to be tokenized) and `encoding` (the encoding to be used for tokenization). 

The endpoint returns a JSON response that includes the total number of tokens, a list of the token IDs, and a list of the token strings.

## Authentication
The application uses HTTP Basic Authentication. The username and password need to be included in the API request.

## Logging
The application includes basic logging. Logs are outputted at the INFO level and above.

## Swagger UI
The application includes a Swagger UI that can be accessed at `/apidocs`.
