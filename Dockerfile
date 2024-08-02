# Using the official Python image as a base
FROM python:3.9-slim

# Working directory in the container
WORKDIR /app

# Copy the getUser.py file into the container
COPY getUser.py .

# Command to run the script
CMD ["python", "getUser.py"]

