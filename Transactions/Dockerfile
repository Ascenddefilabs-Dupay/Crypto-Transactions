FROM python:3.11-slim

WORKDIR /Transactions

COPY requirements.txt /Transactions/
RUN pip3 install -r /Transactions/requirements.txt

COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8016"]