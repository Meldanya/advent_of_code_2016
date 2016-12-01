import argparse
import re


def turn(direction):
    return 1 if 'R' in direction else -1


def walk(instructions):
    pos = (0, 0)
    facing = 0

    for i in instructions:
        dist = int(re.search(r'\d+', i).group())
        facing = (facing + turn(i)) % 4
        if facing == 0:  # N
            pos = (pos[0], pos[1]+dist)
        elif facing == 1:  # E
            pos = (pos[0]+dist, pos[1])
        elif facing == 2:  # S
            pos = (pos[0], pos[1]-dist)
        else:  # W
            pos = (pos[0]-dist, pos[1])

    return abs(pos[0]) + abs(pos[1])


def main(args):
    with open(args.input, 'r') as f:
        inp = f.read()
    instructions = [i.strip() for i in inp.split(',')]
    print(walk(instructions))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('input', type=str, help="Input with walking instructions.")
    main(ap.parse_args())
