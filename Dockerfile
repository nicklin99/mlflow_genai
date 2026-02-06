FROM python:3.12-slim-bookworm

RUN pip install --upgrade 'mlflow[genai]'

CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "5000"]