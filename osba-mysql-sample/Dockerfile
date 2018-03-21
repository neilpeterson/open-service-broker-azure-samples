FROM python

RUN pip install mysqlclient

ADD ./osba-mysql-demo.py /app/osba-mysql-demo.py

CMD ["/bin/sh", "-c", "python -u /app/osba-mysql-demo.py"]