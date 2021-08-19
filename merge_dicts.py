from argparse import ArgumentParser
from glob import glob

from utils import serialize_json
from utils import save_json
from utils import check_for_dict

# python merge_dicts.py -dicts_folder storage/dicts_to_merge/*.json -save_path storage/merged_dict.json

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-dicts_folder', type=str, required=True, help='Path to json file to sort')
    parser.add_argument('-save_path', type=str, required=True, help='Path where to save sorted dict'),
    args = parser.parse_args()

    dicts = [serialize_json(i) for i in glob(args.dicts_folder)]
    for d in dicts:
        check_for_dict(d)

    final_dict = {}
    for d in dicts:
        final_dict.update(d)

    save_json(final_dict, args.save_path)
