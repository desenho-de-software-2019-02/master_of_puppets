FROM ubuntu
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN apt-get install -y python3-pip

RUN mkdir /code
WORKDIR /code

ADD . /code/
RUN pip3 install -r requirements.txt

RUN  chmod +x run.sh

CMD ["./run.sh"]
