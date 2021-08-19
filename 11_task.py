from argparse import ArgumentParser

from utils import serialize_json

# python 11_task.py -first_list storage/ten_task.json -second_list storage/first_last_item.json

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-first_list', type=str, required=True, help='Path to json file')
    parser.add_argument('-second_list', type=str, required=True, help='Path to json file')
    args = parser.parse_args()

    first_list = serialize_json(args.first_list)
    if not isinstance(first_list, list):
        raise TypeError(f'{first_list} should be the type of list')

    second_list = serialize_json(args.second_list)
    if not isinstance(second_list, list):
        raise TypeError(f'{second_list} should be the type of list')

    print(list([i for i in first_list if i not in second_list]))
