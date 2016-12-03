import argparse


def parse_input(fi):
    lines = []
    with open(fi, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def next_step(current, move):
    x, y = current
    if move == 'D':
        return (x, min(y + 1, 2))
    elif move == 'U':
        return (x, max(y - 1, 0))
    elif move == 'L':
        return (max(x - 1, 0), y)
    elif move == 'R':
        return (min(x + 1, 2), y)


def next_step2(current, move):
    x, y = current
    next_ = (x, y)
    if move == 'U' and (y > 0 or abs(x) + abs(y) < 2):
        next_ = (x, y - 1)
    elif move == 'D' and (y < 0 or abs(x) + abs(y) < 2):
        next_ = (x, y + 1)
    elif move == 'L' and (x > 0 or abs(x) + abs(y) < 2):
        next_ = (x - 1, y)
    elif move == 'R' and (x < 0 or abs(x) + abs(y) < 2):
        next_ = (x + 1, y)
    return next_


def to_number2(current):
    return {(0, -2): '1',
            (-1, -1): '2', (0, -1): '3', (1, -1): '4',
            (-2, 0): '5', (-1, 0): '6', (0, 0): '7', (1, 0): '8', (2, 0): '9',
            (-1, 1): 'A', (0, 1): 'B', (1, 1): 'C', (0, 2): 'D'
            }[current]


def to_number(current):
    x, y = current
    return str(x + y*3 + 1)


def walk(lines, step, to_number, start=(1, 1)):
    current = start
    code = []
    for line in lines:
        for move in line:
            current = step(current, move)
        code.append(to_number(current))
    return code


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input', type=str)
    args = ap.parse_args()
    lines = parse_input(args.input)

    # First part
    res = walk(lines, next_step, to_number)
    print(''.join(res))

    # Second part
    res2 = walk(lines, next_step2, to_number2, start=(-2, 0))
    print(''.join(res2))


if __name__ == '__main__':
    main()
