# mlflow-sample
## 1. Setup docker containers

Move to [docker](docker) directory, and build docker images.

```bash
$ docker-compose build
```

Building docker images will be successfully completed if you can find docker images.

```bash
$ docker images
REPOSITORY         TAG       IMAGE ID       CREATED        SIZE
mlflow-training    v0.1      0a7b6e49db01   10 minutes ago   9.99GB
mlflow-server      v0.1      ac9069a69b58   11 minutes ago   2.33GB
```

If you have done that, run the docker containers.

```bash
$ docker-compose up -d
 - Network mlflow-tutorial_default   Created
 - Container mlflow-training         Started
 - Container mlflow-server           Started
```
