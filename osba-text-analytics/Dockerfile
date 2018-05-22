FROM python

RUN pip install requests

ADD ./osba-text-analytics-demo.py /app/osba-text-analytics-demo.py

CMD ["/bin/sh", "-c", "python -u /app/osba-text-analytics-demo.py"]