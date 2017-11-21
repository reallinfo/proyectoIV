FROM python:3
MAINTAINER Alberto del Río


RUN apt-get install -y git
RUN git clone https://github.com/berbus/proyectoIV.git proyecto

RUN pip3 install -r proyecto/requeriments.txt
RUN ls

WORKDIR proyecto/

ENV PORT 80

CMD [ "python3", "./main.py" ]

EXPOSE 80
