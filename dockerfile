FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt.
RUN pip install -r requirements.txt
COPY num.py.
EXPOSE 8082
CMD ["python", "num.py"]
