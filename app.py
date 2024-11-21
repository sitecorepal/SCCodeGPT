from flask import Flask, jsonify, request
from Chat import get_chat_response
import json
# Initialize the Flask app
app = Flask(__name__)

# Define a route for the default URL ("/")
@app.route('/')
def home():
    return "Welcome to Sitecore Code GPT!"

# Define a POST API endpoint
@app.route('/api/chat', methods=['POST'])

def post_data():
    data = request.json  # Get the JSON data from the request
    query = data.get('query')
    result = get_chat_response(query=query)
    response = {
        "result": result
    }
    return jsonify(response)

# Run the Flask app on localhost
if __name__ == '__main__':
    app.run(debug=True)
