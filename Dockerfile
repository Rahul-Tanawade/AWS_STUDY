FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir scikit-learn pandas joblib

CMD ["python" , "main.py"]