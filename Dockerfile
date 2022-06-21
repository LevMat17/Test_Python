FROM python:3

WORKDIR /srv/app/

COPY Makefile ./
COPY app/ ./
COPY requirements.txt requirements.txt
RUN make install

EXPOSE 5000

CMD ["python", "./app.py"]
