FROM python:3.12-slim-bookworm

ENV MLFLOW_ENABLE_ASYNC_TRACE_LOGGING=true

COPY requirements.txt .
RUN pip install -r requirements.txt

# docker run -dp 18500:5000 registry.cn-hangzhou.aliyuncs.com/ktools/mlflow_genai mlflow server --host 0.0.0.0 --port 5000 --allowed-hosts "*"
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000", "--allowed-hosts", "*", "--app-name", "basic-auth"]
