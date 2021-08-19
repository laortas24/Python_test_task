from argparse import ArgumentParser

# python task_five.py -n_rows 10


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-n_rows', type=int, required=True, help='N rows to print')
    args = parser.parse_args()

    row = [1]
    for i in range(args.n_rows):
        print(row)
        row = [sum(x) for x in zip([0] + row, row + [0])]
