# Dockerfile for the nodes (clients)

FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the client code into the container
COPY clientNode.py /app/

# Install any dependencies required for the client
RUN pip install flwr

# Command to run the client when the container starts
CMD ["python", "clientNode.py"]

