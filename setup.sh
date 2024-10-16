#!/usr/bin/zsh

# Build the Docker image with the tag 'mazemaster420'
docker build -t mazemaster420 .

# Run the Docker container, mapping port 5000 of the container to port 5000 on the host
docker run -p 5000:5000 mazemaster420:latest