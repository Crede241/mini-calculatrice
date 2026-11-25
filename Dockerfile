FROM python:3.12-slim
WORKDIR /app
COPY calculatrice.py app.py ./
ENTRYPOINT ["python", "app.py"]