# AI Chatbot (Chainlit + Gemini API)

## Overview
This project is an advanced AI chatbot built using [Chainlit](https://www.chainlit.io/) and Google's Gemini API, with an agent-based architecture provided by a custom or SDK-based `agents` module. The chatbot is designed to provide helpful, conversational responses and can be easily extended or integrated into other applications.

## Features
- Conversational AI assistant powered by Gemini API (Google)
- Agent-based architecture for modularity and extensibility
- Real-time chat interface using Chainlit
- Environment-based configuration for API keys
- Error handling for API and network issues

## Requirements
- Python 3.8+
- [Chainlit](https://www.chainlit.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)
- [openai](https://pypi.org/project/openai/) (for exception handling)
- The `agents` SDK/module (must be available in your environment)

## Installation
1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd chatbot
   ```
2. **Set up a virtual environment (recommended):**
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   # Or, if using uv:
   uv pip install -r requirements.txt
   ```
   > **Note:** Ensure the `agents` SDK/module is installed or available in your Python path.

## Environment Setup
Create a `.env` file in the project root with your Gemini API key:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

## Running the Chatbot
Start the Chainlit server with your main script:

```sh
chainlit run main.py -w
```

This will launch a local web interface where you can interact with the chatbot.

## Configuration
- **API Key:** The Gemini API key is loaded from the `.env` file.
- **Agents SDK:** Ensure the `agents` module is available (either as a package or in your project directory).

## Usage
- Open your browser to the URL provided by Chainlit (usually [http://localhost:8000](http://localhost:8000)).
- Start chatting with the AI assistant!

## Troubleshooting
- **ModuleNotFoundError: No module named 'agents'**
  - Ensure the `agents` SDK/module is installed or available in your project.
- **GEMINI_API_KEY is not set**
  - Make sure your `.env` file exists and contains a valid API key.
- **Dependency conflicts**
  - Use a clean virtual environment to avoid package version issues.
- **Other errors**
  - Check the console output for detailed error messages.

## Example .env
```
GEMINI_API_KEY=your_gemini_api_key_here
```

## License
Specify your license here.

## Acknowledgments
- [Chainlit](https://www.chainlit.io/)
- [Google Gemini API](https://ai.google.dev/gemini-api/docs/openai)
- The authors of the `agents` SDK/module
