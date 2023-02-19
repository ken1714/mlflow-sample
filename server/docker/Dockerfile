FROM python:3.10

# Dependencies
RUN pip3 install mlflow[extras]

# open port 5000
EXPOSE 5000

# Start mlflow server
CMD mlflow server \
    --host 0.0.0.0 \
    --port 5000
