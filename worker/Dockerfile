FROM python:3.11-slim
COPY worker.py .
RUN pip install flask requests
CMD ["python", "worker.py"]