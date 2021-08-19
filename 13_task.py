from argparse import ArgumentParser

# python 13_task.py -number 12345

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-number', type=str, required=True, help='Number to parse')
    args = parser.parse_args()

    print(sum([int(i) for i in args.number]))
