from argparse import ArgumentParser

from utils import serialize_json
from utils import save_json
from utils import check_for_dict
from utils import number2base

# python four_task.py -path_to_file storage/four_task.json -save_path storage/four_task_result.json -numeral_system 2

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-path_to_file', type=str, required=True, help='Path to json file to sort')
    parser.add_argument('-save_path', type=str, required=True, help='Path where to save sorted dict'),
    parser.add_argument(
        '-numeral_system', type=int, required=True,
        help='Numeral system to process number', choices=[2, 8, 10, 16]
    )

    args = parser.parse_args()

    file = serialize_json(args.path_to_file)
    check_for_dict(file)

    number = file.get('number', None)
    if number is None:
        raise KeyError('You need to pass number in dict')

    if not isinstance(number, int):
        raise TypeError('Number should be type of int')

    file['number'] = number2base(file['number'], args.numeral_system)
    save_json(file, args.save_path)

