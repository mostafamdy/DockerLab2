# Q2
Troubleshooting

##  How to start:
- docker build -t q4:1 .
- docker run --name redis-container redis 
- docker run -p 8080:80 -e APP_PORT=80 -e REDIS_HOST=redis-container -e REDIS_PORT=6379 --link redis-container q4:2 
 

## images

