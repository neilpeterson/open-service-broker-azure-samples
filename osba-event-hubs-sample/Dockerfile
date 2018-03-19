FROM python

RUN pip install azure-storage-blob

ADD ./osba-storage-demo.py /app/osba-storage-demo.py

CMD ["/bin/sh", "-c", "python -u /app/osba-storage-demo.py > kubelog.log 2>&1"]