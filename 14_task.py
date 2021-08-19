from argparse import ArgumentParser

# python 14_task.py -text asdasdasd -char a

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-text', type=str, required=True, help='Number to parse')
    parser.add_argument('-char', type=str, required=True, help='Char to count')
    args = parser.parse_args()

    counter = 0
    for i in args.text:
        if i == args.char:
            counter += 1

    print(counter)
