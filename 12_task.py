from argparse import ArgumentParser
from glob import glob
import os

# python 12_task.py -path_to_file storage

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-path_to_file', type=str, required=True, help='Path to json file')
    args = parser.parse_args()

    if not os.path.exists(args.path_to_file):
        raise FileNotFoundError(f'{args.path_to_file} path does not exist')

    files = glob(args.path_to_file + '/*')
    print(sorted(files, key=lambda t: -os.stat(t).st_mtime))
