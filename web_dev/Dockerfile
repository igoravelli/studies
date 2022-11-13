FROM python:latest

WORKDIR /home/igorregly/Test_Docker

COPY . .

USER root

RUN apt-get -y update
RUN apt install pip -y
RUN pip install pandas
RUN pip install numpy

CMD ["python", "--version"]