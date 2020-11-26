FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./Pipfile Pipfile.lock ./
RUN pip install pipenv \
 && pipenv install --system --deploy

COPY ./ /app
