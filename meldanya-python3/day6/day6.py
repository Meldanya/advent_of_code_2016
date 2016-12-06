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
    messages = [''] * 2
    for col in cols:
        messages[0] += most_common(col)
        messages[1] += least_common(col)
    print('\n'.join(messages))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input', type=str)
    args = ap.parse_args()
    decode(args.input)


if __name__ == '__main__':
    main()
