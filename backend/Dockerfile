FROM python:3.9-slim 

# install poetry 
RUN pip install pdm

# copy project requirement files 
COPY pyproject.toml pdm.lock ./

# install runtime deps
RUN pdm install
RUN pdm venv activate

COPY ./app ./

ENV PATH=.venv/bin/

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]