FROM python:3

EXPOSE 5000/tcp

WORKDIR /app

COPY simple_flask_rest_api/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY simple_flask_rest_api /app

CMD [ "python", "./app.py" ]
