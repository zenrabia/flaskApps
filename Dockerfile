FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

# CMD [ "python", "-m","flask", "--app", "main.py", "run", "--host=127.0.0.1"]
CMD ["python","-m","main"]