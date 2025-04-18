FROM python:3

WORKDIR /usr/src/app

COPY python_code/ ./

ENTRYPOINT [ "python","portScanner.py" ]
CMD ["--port","80","--ip","8.8.8.8"]

#docker run q2:1 --ip 8.8.8.8 --port 443
