FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile","Pipfile.lock","./"]

RUN pipenv install --system --deploy

COPY ["Predict_city.py","Predict_resort.py", "/Models","./"]

EXPOSE 9697

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9697", "Predict_resort:app"]