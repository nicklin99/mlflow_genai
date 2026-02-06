

## mysql

docker run --env MLFLOW_FLASK_SERVER_SECRET_KEY='my-secret-key' --env MLFLOW_BACKEND_STORE_URI='mysql+pymysql://root@localhost:3306/mlflow' -p 18500:5000 registry.cn-hangzhou.aliyuncs.com/ktools/mlflow_genai