# mlflow-sample
## 1. Setup docker containers

Move to [docker](docker) directory, and build docker image.

```bash
$ docker-compose build
```

Building docker image will be successfully completed if you can find a docker image named `mlflow-tutorial`.

```bash
$ docker images
REPOSITORY         TAG       IMAGE ID       CREATED        SIZE
mlflow-tutorial    v0.1      a65f6ae93390   11 days ago    9.99GB
```

If you have done that, run the docker containers.

```bash
$ docker-compose up -d
 - Network mlflow-tutorial_default   Created
 - Container mlflow-server           Started
 - Container mlflow-training-server  Started
```
