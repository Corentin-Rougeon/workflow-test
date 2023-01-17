FROM python:3.9

WORKDIR /app

COPY app.py .

CMD [ "python", "-m", "unittest", "test_simplemath.py" ]