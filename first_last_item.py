from argparse import ArgumentParser

from utils import serialize_json

# python first_last_item.py -path_to_file storage/first_last_item.json

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-path_to_file', type=str, required=True, help='Path to json file to sort')
    args = parser.parse_args()

    file = serialize_json(args.path_to_file)
    if not isinstance(file, list):
        raise TypeError(f'{file} should be type of list')

    if not file:
        raise ValueError(f'{file} is empty')

    print(file[0], file[-1])
