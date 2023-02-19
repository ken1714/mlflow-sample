import argparse
import os
import pandas as pd
from sklearn.model_selection import train_test_split


def main(csv_path, output_dir, random_seed):

    # Read the wine-quality csv file from the URL
    data = pd.read_csv(csv_path)

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data, random_state=random_seed)

    # Save training and test data
    if output_dir is None:
        output_dir = os.path.dirname(csv_path)
    os.makedirs(output_dir, exist_ok=True)
    csv_name = os.path.splitext(os.path.basename(csv_path))[0]
    train.to_csv(os.path.join(output_dir, f"{csv_name}_train.csv"), index=False)
    test.to_csv(os.path.join(output_dir, f"{csv_name}_test.csv"), index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split dataset to training data and test data.")
    parser.add_argument("csv_path", type=str)
    parser.add_argument("--output_dir", default=None, type=str)
    parser.add_argument("--random_seed", "-s", default=40, type=int)

    args = parser.parse_args()
    main(args.csv_path, args.output_dir, args.random_seed)
