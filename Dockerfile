FROM python:3.9

RUN python -m pip install --upgrade pip

WORKDIR /PythonServer

COPY main.py .

ENTRYPOINT ["python", "main.py"]
