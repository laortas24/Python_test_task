from argparse import ArgumentParser

# python seven_task.py -numbers 0,1,2.3,5

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-numbers', type=str, required=True, help='Numbers to save')
    args = parser.parse_args()

    parsed_numbers = []
    for i in args.numbers.split(','):
        try:
            parsed_numbers.append(int(i))
        except ValueError:
            parsed_numbers.append(float(i))

    tuple_numbers = tuple(parsed_numbers)

    print(f'List: {parsed_numbers}\nTuple: {tuple_numbers}')
