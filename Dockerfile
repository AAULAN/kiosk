FROM python:3-slim
COPY / /
RUN pip install -r requirements.txt
CMD ["gunicorn", "-w", "1", "-k", "gevent", "manage:app"]

EXPOSE 8000