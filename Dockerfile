# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install SQLite CLI
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Copy dependency list and install
COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy code and data
COPY app/ ./app
COPY data/ /data

# Set default command
CMD ["python", "app/pipeline.py"]
