#!/bin/bash

docker-compose -f \
    ./api_gateway/docker-compose.yml \
    up --build -d