from argparse import ArgumentParser
import os

# python nine_task.py -path_to_file storage/dict_to_sort.json

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-path_to_file', type=str, required=True, help='Path to json file to sort')
    args = parser.parse_args()

    filename, file_extension = os.path.splitext(args.path_to_file)
    if not file_extension:
        raise ValueError('file does not have an extension')

    print(file_extension)
