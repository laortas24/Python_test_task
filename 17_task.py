from argparse import ArgumentParser

from utils import serialize_json

# python 17_task.py -text 'asd asd asd das das ajsdklajsldkajsldk'

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-text', type=str, required=True, help='Text to parse')
    args = parser.parse_args()

    word_counter = {}
    longest = ''
    for i in args.text.split():
        if i not in word_counter:
            word_counter[i] = 1
        else:
            word_counter[i] += 1

        if len(i) > len(longest):
            longest = i

    most_frequent = max(word_counter, key=lambda x: word_counter[x])
    print(f'Longest: {longest} Most frequent: {most_frequent}')
