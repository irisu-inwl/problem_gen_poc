FROM python:3.10

RUN apt update \
  && apt upgrade -y
RUN apt install -y wget curl

RUN useradd -m -u 1000 app \
  && mkdir /opt/app \
  && chown app:app /opt/app 

USER 1000
WORKDIR /opt/app

ENV POETRY_VERSION=1.2.0
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/home/app/.local/bin:$PATH"

COPY poetry.lock .
COPY pyproject.toml .
COPY src .

RUN poetry install --no-root

CMD poetry run streamlit run app.py
