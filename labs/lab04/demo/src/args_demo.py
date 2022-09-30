import sys


def force(m, g):
    return m * g


def parse(args):
    m = float(args[0])
    g = float(args[1])

    return m, g


if __name__ == '__main__':
    m, g = parse(sys.argv[1:])
    f = force(m, g)

    print(f)
