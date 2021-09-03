FROM python:3

# equivaut à mkdir app puis cd app
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

RUN chmod +x app.py

CMD [ "python3", "app.py" ]