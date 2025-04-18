# Q3
Create a dockerfile for ubuntu image which sleeps according to the given number in the docker command argument, If no arguments were provided then it defaults to 15 seconds, then try to override the sleep command altogether and echo “entrypoint overridden”. 

##  How to start:
- docker build -t q3:1 .
- docker run --entrypoint echo q3:1 Hello world

## images

