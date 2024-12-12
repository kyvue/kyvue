# Base image with Python
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    FLASK_APP=kyvue.app

# Set the working directory
WORKDIR /app

# Copy only the requirements file first to leverage Docker caching
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port the Flask app runs on
EXPOSE 5000

# Set the default command to run the Flask application
ENTRYPOINT ["python", "run.py"]
