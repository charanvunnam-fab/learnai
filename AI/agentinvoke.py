import os
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

agent = create_agent(
    model="groq:qwen/qwen3-32b",
     tools=[],
    system_prompt="You are a helpful assistant that can give captials of the world in a single line")
response =agent.invoke(
    {"messages": [{"role": "user", "content": "What is the capital of France?"}]})
print(response)
