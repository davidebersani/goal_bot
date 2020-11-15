#publicly available docker image "python" on docker hub will be pulled

FROM python:3

#creating directory in container (linux machine)

RUN mkdir c:\home 

COPY requirements.txt /home/requirements.txt

RUN pip3 install -r /home/requirements.txt

COPY src/praw.ini /usr/local/lib/python3.8/site-packages/praw/praw.ini
COPY src/ /home/src

#running script in container

CMD python -u /home/src/main.py