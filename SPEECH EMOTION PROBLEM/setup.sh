#!/bin/bash

echo Beginning process!

# Build Docker Image
docker build ./context -t sumit/meld:v1

# Create Docker container
docker kill sumit_image
docker rm -v $(docker ps --filter status=exited -q)
docker run -dit --mount src="$1",target=/home/ubuntu/test,type=bind --name sumit_image sumit/meld:v1

# Run python function to generate predictions
docker exec -it sumit_image python output.py

# Copy the output file generated back to the host machine
docker cp sumit_image:/home/ubuntu/output.txt ./