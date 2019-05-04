FROM python:3.6
COPY / /
RUN pip install -r requirements.txt
CMD ["gunicorn", "-w", "1", "-k", "gevent", "-b", "0.0.0.0:8000", "manage:app"]

EXPOSE 8000