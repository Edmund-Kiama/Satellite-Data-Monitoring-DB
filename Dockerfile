FROM python:3.8-slim

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock" ,"./"]
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile 

COPY . .

CMD ["pipenv", "run", "python", "main.py"]
