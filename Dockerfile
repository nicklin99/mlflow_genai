FROM python:3.12-slim-bookworm

RUN pip install --upgrade 'mlflow[genai]'
RUN pip install 'mlflow[auth]'
# docker run -dp 18500:5000 registry.cn-hangzhou.aliyuncs.com/ktools/mlflow_genai mlflow server --host 0.0.0.0 --port 5000 --allowed-hosts "*"
CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000", "--allowed-hosts", "*", "--app-name", "basic-auth"]
