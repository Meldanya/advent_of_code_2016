import argparse
import re

RE = re.compile(r'(\d+)\[(.*)\]$')

def sort(occurances):
    dupes = [n for _, n in occurances]
    dupes = set([n for i, n in enumerate(dupes) if n in dupes[i+1:]])
    res, rest = [], []
    prev = -1
    for c, n in occurances:
        if rest and n < prev:
            res.extend(sorted(rest))
            rest = []

        if n not in dupes:
            res.append(c)
        else:
            rest.append(c)
        prev = n
    return res + sorted(rest)


def is_valid(room):
    name, _, maybe_checksum = room
    chars = list(name)
    occurances = {c: chars.count(c) for c in chars if not c == '-'}
    occurances = sorted(occurances.items(), key=lambda x: x[1], reverse=True)
    checksum = ''.join(sort(occurances))[:5]
    return checksum[:5] == maybe_checksum


def _parse_room(line):
    end_of_name = line.rfind('-')
    name, rest = line[:end_of_name], line[end_of_name+1:]
    m = RE.match(rest)
    if not m:
        raise ValueError("Bad input: %s" % line)
    sector, checksum = m.groups()
    return (name, int(sector), checksum)


def parse_input(fi):
    lines = []
    with open(fi, 'r') as f:
        lines = f.read().splitlines()
    return [_parse_room(line) for line in lines]


def decrypt(rooms):
    def _shift(c, n):
        return chr((ord(c) - ord('a') + n) % 26 + ord('a'))
    decrypted = []
    for room in rooms:
        name, sector, ch = room
        decrypted_name = [_shift(n, sector) if not n == '-' else ' '
                          for n in name]
        decrypted.append((''.join(decrypted_name), sector, ch))
    return decrypted


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input', type=str)
    args = ap.parse_args()
    rooms = parse_input(args.input)

    # Part 1
    valid = [r for r in rooms if is_valid(r)]
    sector_sum = sum([sector for _, sector, _ in valid])
    print(sector_sum)

    # Part 2
    northpole_object_storage = [(n, s, c)
                                for (n, s, c) in decrypt(valid)
                                if 'north' in n]
    print(northpole_object_storage)


if __name__ == '__main__':
    main()
