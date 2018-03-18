FROM python

RUN pip install pymongo

ADD ./osba-cosmos-mongodb-demo.py /app/osba-cosmos-mongoddb-demo.py

CMD ["/bin/sh", "-c", "python -u /app/osba-cosmos-mongoddb-demo.py"]