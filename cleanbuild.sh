#!/bin/bash
docker kill test5container
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
docker build -t test5image .
docker run -d -p 80:80 --name test5container test5image
