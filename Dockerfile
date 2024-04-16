FROM python:latest
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD pytest HW_18_database/tests