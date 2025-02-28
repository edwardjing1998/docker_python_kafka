# Dockerfile
FROM python:3.9-slim

# Create a directory for your app
WORKDIR /app

# Copy requirements first and install
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . /app/

# Expose port 7500 *internally* (the actual container's Flask port)
EXPOSE 7500

# Default command (also overridden by docker-compose if needed)
CMD ["python", "-u", "app/main.py"]
