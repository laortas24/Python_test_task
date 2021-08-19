from argparse import ArgumentParser

from utils import serialize_json
from utils import save_json
from utils import check_for_dict

# python find_top_three.py -path_to_file storage/find_top_three.json -save_path storage/top_three.json

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-path_to_file', type=str, required=True, help='Path to json file to sort')
    parser.add_argument('-save_path', type=str, required=True, help='Path where to save sorted dict'),
    args = parser.parse_args()

    dict_to_sort = serialize_json(args.path_to_file)
    check_for_dict(dict_to_sort)
    sorted_dict = sorted(dict_to_sort, key=lambda x: int(dict_to_sort[x]), reverse=True)[:3]
    save_json(sorted_dict, args.save_path)
