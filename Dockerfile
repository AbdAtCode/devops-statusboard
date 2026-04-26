# Start from official Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy dependencies file first
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the app
COPY app/ .

# Tell Docker this app runs on port 5000
EXPOSE 5000

# Command to run the app
CMD ["python3", "app.py"]
