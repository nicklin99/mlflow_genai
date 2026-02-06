from openai import OpenAI
import mlflow
from dotenv import load_dotenv
import httpx
load_dotenv()

http_client = httpx.Client(
    auth=(os.getenv("MLFLOW_TRACKING_USERNAME"), os.getenv("MLFLOW_TRACKING_PASSWORD")),
)

client = OpenAI(
    base_url="http://localhost:18500/gateway/mlflow/v1",
    api_key="",  # API key not needed, configured server-side
    http_client=http_client,
)
mlflow.set_tracking_uri("http://localhost:18500")
mlflow.set_experiment("Default")
mlflow.openai.autolog()
prompt = mlflow.genai.load_prompt("prompts:/hello/2")

messages = [{"role": "user", "content": prompt.format(name="你是谁"),}]
print(messages)

response = client.chat.completions.create(
    model="aliyun",  # Endpoint name as model
    messages=messages,
)
print(response.choices[0].message)