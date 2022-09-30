import sys
from argparse import ArgumentParser


def force(m, g):
    return m * g


def parse(args):

    return m, g


if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('-m', '--mass', type=float)
    parser.add_argument('-g', type=float)

    args = parser.parse_args()
    
    f = force(args.mass, args.g)

    print(f)
