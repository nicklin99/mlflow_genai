import os
from openai import OpenAI
import mlflow
# load .env
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# Set MLflow tracking URI
mlflow.set_tracking_uri("http://localhost:18500")
mlflow.set_experiment("Default")
mlflow.openai.autolog()
# Example of loading and using the prompt
prompt = mlflow.genai.load_prompt("prompts:/hello/1")
response = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": prompt.format(name="你是谁？"),
    }],
    model="qwen-flash",
)

print(response.choices[0].message.content)