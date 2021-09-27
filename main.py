import sys
from argparse import ArgumentParser

def main(args):
    data = []
    with open(args.file_location, "r") as f:
        data = f.readlines()

    print(data)

if __name__ == "__main__":
    parser = ArgumentParser('main.py')
    parser.add_argument('file_location', help='location of file to load')

    args = parser.parse_args()
    main(args)
