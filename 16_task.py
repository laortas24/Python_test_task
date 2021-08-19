from argparse import ArgumentParser

from utils import serialize_json

# python 16_task.py -path_to_file storage/15_task.json

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-path_to_file', type=str, required=True, help='Path to json file')
    args = parser.parse_args()

    file = serialize_json(args.path_to_file)
    if not isinstance(file, list):
        raise TypeError(f'{file} should be the type of list')

    unique_numbers = set([i for i in file if isinstance(i, (int, float))])

    print(len(unique_numbers) == len([i for i in file if isinstance(i, (int, float))]))
