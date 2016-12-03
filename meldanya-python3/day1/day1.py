import argparse
import re


def turn(direction):
    return 1 if 'R' in direction else -1


def visit(prev, pos):
    """Return a list of every position between the two arguments."""
    diff_x = pos[0] - prev[0]
    diff_y = pos[1] - prev[1]
    # We either move in x or y direction, never both.
    if diff_x:
        visited = [(r, pos[1]) for r in range(prev[0], pos[0],
                                              1 if diff_x > 0 else -1)]
    else:
        visited = [(pos[0], r) for r in range(prev[1], pos[1],
                                              1 if diff_y > 0 else -1)]
    return visited


def walk(instructions):
    visited = []
    twice = []
    pos = (0, 0)
    facing = 0

    for i in instructions:
        dist = int(re.search(r'\d+', i).group())
        facing = (facing + turn(i)) % 4
        prev = pos
        if facing == 0:  # N
            pos = (pos[0], pos[1]+dist)
        elif facing == 1:  # E
            pos = (pos[0]+dist, pos[1])
        elif facing == 2:  # S
            pos = (pos[0], pos[1]-dist)
        else:  # W
            pos = (pos[0]-dist, pos[1])

        # Visit every point between the positions.
        new_visit = visit(prev, pos)
        for v in new_visit:
            if v in visited:
                twice.append(v)
        visited.extend(new_visit)

    res = twice[0]
    return abs(pos[0]) + abs(pos[1]), abs(res[0]) + abs(res[1])


def main(args):
    with open(args.input, 'r') as f:
        inp = f.read()
    instructions = [i.strip() for i in inp.split(',')]
    print(walk(instructions))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('input', type=str, help="Input with walking instructions.")
    main(ap.parse_args())
