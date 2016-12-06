import argparse
import collections


def most_common(s):
    return collections.Counter(s).most_common(1)[0][0]


def least_common(s):
    return collections.Counter(s).most_common()[-1][0]


def decode(in_file):
    with open(in_file) as f:
        lines = f.read().splitlines()
    cols = list(zip(*lines))
    message1, message2 = '', ''
    for col in cols:
        message1 += most_common(col)
        message2 += least_common(col)
    print(message1)
    print(message2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input', type=str)
    args = ap.parse_args()
    decode(args.input)


if __name__ == '__main__':
    main()
