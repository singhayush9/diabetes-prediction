# Use the official Python 3.8 image from Docker Hub
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 5000

# Define the command to run the Flask app
CMD ["python", "app.py"]


# docker build -t diabetes-app .
# docker run -d -p 5000:5000 diabetes-app

