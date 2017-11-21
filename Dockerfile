FROM python:3
MAINTAINER Alberto del Río


RUN apt-get install -y git
RUN git clone https://github.com/berbus/proyectoIV.git proyecto

RUN pip3 install -r ./proyecto/requeriments.txt

WORKDIR ./proyecto/

ENV PORT 8000

CMD [ "python3", "./main.py" ]

EXPOSE 8000
