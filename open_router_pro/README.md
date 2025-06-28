# Open Router Pro

A Python application that demonstrates how to use OpenRouter API with AI agents for creative writing tasks. This project showcases integration between OpenRouter's model marketplace and the OpenAI Agents framework.

## Features

- 🤖 **AI Agent Integration**: Uses OpenAI Agents framework for structured AI interactions
- 🌐 **OpenRouter API**: Connects to OpenRouter's model marketplace for access to various AI models
- ✍️ **Creative Writing**: Specialized writer agent for story generation
- 🔧 **Flexible Configuration**: Easy model switching and configuration management
- 🔒 **Environment Security**: Secure API key management using environment variables

## Prerequisites

- Python 3.12 or higher
- OpenRouter API key
- Gemini API key (for additional functionality)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd open_router_pro
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -e .
   ```

## Configuration

1. **Create a `.env` file** in the project root:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

2. **Get your API keys**:
   - [OpenRouter API Key](https://openrouter.ai/keys) - Sign up and get your API key
   - [Gemini API Key](https://ai.google.dev/) - Get your Gemini API key (optional)

## Usage

Run the main application:

```bash
python main.py
```

The application will:
1. Load your API keys from environment variables
2. Initialize an OpenRouter client with the Mistral model
3. Create a writer agent with creative writing instructions
4. Process the input prompt and generate a story response

## Current Configuration

- **Model**: `mistralai/mistral-small-3.2-24b-instruct:free`
- **Agent Type**: Writer assistant
- **Agent Instructions**: "you are a writer assistant and write stories"
- **Input Example**: "covid is not over its mutate"

## Customization

### Changing Models

You can easily switch to different models available on OpenRouter by modifying the model name in `main.py`:

```python
model = OpenAIChatCompletionsModel(
    model="anthropic/claude-3.5-sonnet",  # Change this line
    openai_client=external_client
)
```

### Modifying Agent Instructions

Update the agent instructions to change the agent's behavior:

```python
agent = Agent(
    name="Your Agent Name",
    instructions="Your custom instructions here"
)
```

### Adding New Inputs

Modify the input in the `Runner.run_sync()` call:

```python
response = Runner.run_sync(
    agent,
    input="Your custom input here",
    run_config=config
)
```

## Project Structure

```
open_router_pro/
├── main.py              # Main application file
├── pyproject.toml       # Project configuration and dependencies
├── README.md           # This file
├── .env                # Environment variables (create this)
└── .venv/              # Virtual environment directory
```

## Dependencies

- `openai-agents>=0.0.19` - OpenAI Agents framework
- `python-dotenv>=1.1.0` - Environment variable management
- `litellm` - Async OpenAI client for OpenRouter integration

## Error Handling

The application includes basic error handling:
- Validates that required API keys are set
- Graceful handling of API connection issues
- Clear error messages for missing configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for more details.

## Support

If you encounter any issues:
1. Check that your API keys are correctly set in the `.env` file
2. Ensure you have sufficient credits in your OpenRouter account
3. Verify your Python version meets the requirements (3.12+)

## Related Links

- [OpenRouter Documentation](https://openrouter.ai/docs)
- [OpenAI Agents Documentation](https://github.com/openai/agents)
- [Mistral AI Models](https://mistral.ai/)
