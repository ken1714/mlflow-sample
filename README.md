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
### 2.1 Split training and test data

Run below command to save training and test data to `--output_dir` as csv files. `--output_dir` and `--random_seed` are options. The directory that has the input csv file will be set as `--output_dir` if you does not set `--output_dir`. There is uniform selection for splitting training and test data, but you can set `--random_seed` to get various splitted results.


```bash
python3 split_train_test.py data/winequality-red.csv --output_dir output --random_seed 40
```

### 2.2 Run training

Run below command. `--alpha` (default: 0.5), `--l1_ratio` (default: 0.5) and `--exp_name` are options. `--exp_name` is display name for mlflow tracking.

```bash
$ python3 train.py train.csv test.csv --exp_name experiment_sample --alpha 0.5 --l1_ratio 0.5
```

## 3. View trained results

Access to http://localhost:8000/ from your host machine.
