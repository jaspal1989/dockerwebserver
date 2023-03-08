FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY webserver.py ./
COPY index.html ./

CMD [ "python3", "./webserver.py" ]
