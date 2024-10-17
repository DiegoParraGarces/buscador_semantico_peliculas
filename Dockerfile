FROM python:3.12-slim

RUN apt-get update && apt-get install -y nano

WORKDIR /app

COPY src/ ./src/
COPY requirements.txt /app/requirements.txt 
COPY src/data/ ./data/

RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*


RUN pip install --no-cache-dir -r requirements.txt

VOLUME ./app/src

CMD [ "python", "./src/infinite_loop.py" ]