FROM python

RUN pip install requests

ADD ./osba-container-instances-demo.py /app/osba-container-instances-demo.py

CMD ["/bin/sh", "-c", "python -u /app/osba-container-instances-demo.py"]