import pandas as pd
import argparse
from dpre import dpre
from eda import eda
from vis import vis
from model import model
def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

def main():
    parser = argparse.ArgumentParser(description="Load a dataset from a file.")
    parser.add_argument("file_path", type=str, help="Path to the dataset file")

    args = parser.parse_args()
    file_path = args.file_path

    # dataset = load_dataset(file_path)

    dataset = dpre(file_path)
    eda(dataset)
    vis(dataset)
    model(dataset)



if __name__ == "__main__":
    main()
