# Builder for installing python packages
# You need a "buster" image to install mlflow and psycopg2
FROM python:3.10.10-buster as builder

# Install mlflow and psycopg2
RUN pip3 install --upgrade pip
RUN pip3 install \
    mlflow \
    mysqlclient

# Main image (smaller size)
FROM python:3.10.10-slim-buster

# Copy the essential packages from the docker image "python:x.x.x-*-buster" to the main docker image
# because the size of the docker image "python:x.x.x-*-buster" is large
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin/mlflow /usr/local/bin/mlflow
COPY --from=builder /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu
COPY --from=builder /lib/x86_64-linux-gnu /lib/x86_64-linux-gnu
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

# Set environment variables
ARG MLFLOW_TRACKING_PORT
ENV MLFLOW_TRACKING_PORT=${MLFLOW_TRACKING_PORT}

# Open port
EXPOSE ${MLFLOW_TRACKING_PORT}
