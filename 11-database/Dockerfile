FROM arm64v8/python:3.10-slim-bullseye

ENV POETRY_VERSION=1.2.2

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /usr/src

ENV PYTHONPATH="$PYTHONPATH:/src/app"

COPY poetry.lock pyproject.toml ./

# This makes to be able to use "uvicorn" without `poetry shell`
RUN poetry config virtualenvs.create false
RUN poetry config installer.parallel false
RUN poetry install --no-interaction --no-ansi

COPY app ./app

# ENTRYPOINT ["uvicorn", "app.main:app", "--reload"]
ENTRYPOINT ["uvicorn", "app.main:app", "--host=0.0.0.0", "--timeout-keep-alive=0", "--port=8000", "--reload"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]