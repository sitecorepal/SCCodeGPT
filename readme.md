**README.md**

# Sitecore Code GPT

This project is a Flask-based API that integrates with Sitecore to provide a conversational AI experience. The API uses the `Chat` module to generate code responses based on user queries based on grounding information.

# How does it work?

![Concept map](<resources/Concept map.png>)

## Getting Started

To set up this project, follow these steps:

1. Install Python 3.x (https://www.python.org/downloads/)
2. Clone this repository or download the project files.
3. Navigate to the project directory in your terminal or command prompt.
4. Install the required dependencies by running: `pip install -r requirements.txt`
5. Create .env file and have following keys populated:
   * `OPENAI_API_KEY`
   * `AZURE_OPENAI_API_KEY`
   * `AZURE_OPENAI_ENDPOINT`

Note: The code uses Azure Open AI for chat and Open AI for embeddings, but you could use your own LLMs.

## Build Embeddings

1. Copy clean reference code to `sc_code` folder to create embeddings. (use Sitecore starter kit to try.)
2. Run python Learn.py to generate embeddings.

## Running the API

1. Start the Flask development server by running: `python app.py`
2. The API will be accessible at `http://localhost:5000/`

## API Endpoints

### POST /api/chat

This endpoint accepts a JSON payload with a `query` parameter and returns a JSON response with the AI's response.

**Request:**

```json
{
  "query": "Create a new promo component for Sitecore XMCloud Headless using typescript."
}
```

## Customizing the Chat Module

The `Chat` module is responsible for generating responses based on user queries. You can customize this module by implementing your own logic or integrating with a third-party AI service.

To use a different AI service, update the `get_chat_response` function in the `Chat` module with the appropriate code to make API requests to the chosen service.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.