# Dockerfile for the central server

FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the server code into the container
COPY serverNode.py /app/

# Install any dependencies required for the server
RUN pip install flwr

# Expose the port on which the server will run (adjust as needed)
EXPOSE 8080

# Command to run the server when the container starts
CMD ["python", "serverNode.py"]
