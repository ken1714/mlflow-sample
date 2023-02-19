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

## 2. Training

Run below command. `--alpha` (default: 0.5) and `--l1_ratio` (default: 0.5) are options.

```bash
$ python3 train.py --alpha 0.5 --l1_ratio 0.5
```

## 3. View trained results

Access to http://localhost:8000/ from your host machine.
