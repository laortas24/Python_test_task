from argparse import ArgumentParser

# python palindrome_check.py -text asddsa


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-text', type=str, required=True, help='Text to check')
    args = parser.parse_args()

    print(args.text == args.text[::-1])
