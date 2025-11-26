FROM python:3.10-slim
COPY calculator.py /calculator.py
CMD ["python3", "/calculator.py"]
