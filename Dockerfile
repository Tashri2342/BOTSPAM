# Use the official Python image as the base image with Python 3.9 tag
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the required files into the container
COPY . /app

# Install system dependencies and Python packages
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y git ffmpeg
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

# Define the command to run your application
CMD python3 -m LegendGirl
