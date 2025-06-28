import os
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, RunConfig, Runner
from litellm import AsyncOpenAI

load_dotenv()

OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY")

gemini_api_key=os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

model = OpenAIChatCompletionsModel(
    model="mistralai/mistral-small-3.2-24b-instruct:free",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
     
agent=Agent(
    name="Writer agent",
    instructions="you are a writer assistant.and write stories"

)

response=Runner.run_sync(
    agent,
    input="covid is not over its mutate",
    run_config=config
)
print(response)
