import os
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, RunConfig, Runner
from litellm import AsyncOpenAI

load_dotenv()
gemini_api_key=os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
     
agent=Agent(
    name="Translator",
    instructions="you are a helpul assistant.and convert english into urdu language"

)

response=Runner.run_sync(
    agent,
    input="covid is not over its mutate",
    run_config=config
)
print(response)
