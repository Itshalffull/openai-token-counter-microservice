import os
import logging
from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from
from flask_httpauth import HTTPBasicAuth
import tiktoken

app = Flask(__name__)
swagger = Swagger(app)
auth = HTTPBasicAuth()
ENCODINGS = ["cl100k_base", "p50k_base", "r50k_base"]

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define users
users = {
    "user1": "password1",
    "user2": "password2"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

@app.route('/tokenize', methods=['POST'])
@auth.login_required
@swag_from('swagger.yaml')
def tokenize_text():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400
    text = data.get('text')
    encoding = data.get('encoding')
    if not text or not encoding:
        return jsonify({'message': 'text and encoding are required'}), 400
    if encoding not in ENCODINGS:
        return jsonify({'message': f'Invalid encoding. Available encodings are {ENCODINGS}'}), 400

    try:
        tokenizer = tiktoken.get_encoding(encoding)
    except Exception as e:
        app.logger.error(f"Error getting encoding: {str(e)}")
        return jsonify({'message': 'Error getting encoding'}), 500

    try:
        tokens = tokenizer.encode(text)
        tokens_strings = [tokenizer.decode_single_token_bytes(token).decode() for token in tokens]
        num_tokens = len(tokens)
        response = {
            'total_tokens': num_tokens,
            'tokens': tokens,
            'tokens_strings': tokens_strings
        }
        return jsonify(response), 200
    except Exception as e:
        app.logger.error(f"Error tokenizing text: {str(e)}")
        return jsonify({'message': 'Error tokenizing text'}), 500

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
