FROM python:3.7

LABEL maintainer="Hanish"

COPY ./app /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 80

# command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
