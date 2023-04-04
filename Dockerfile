FROM python:3.9-slim

EXPOSE 8080

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0"]