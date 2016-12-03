import argparse


def parse_input(fi):
    lines = []
    with open(fi, 'r') as f:
        lines = f.readlines()
    triangles = [tuple([int(t) for t in line.split()]) for line in lines]
    return triangles


def valid(tri):
    return (tri[0] + tri[1] > tri[2] and
            tri[1] + tri[2] > tri[0] and
            tri[2] + tri[0] > tri[1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('input', type=str)
    args = ap.parse_args()
    triangles = parse_input(args.input)

    # Part 1
    valid_triangles = [tri for tri in triangles if valid(tri)]
    print(len(valid_triangles))

    # Part 2
    valid_triangles = []
    while triangles:
        tris = triangles[:3]
        triangles = triangles[3:]
        # Nice way to compute matrix transpose:
        tris = list(zip(*tris))
        valid_triangles.extend([tri for tri in tris if valid(tri)])

    print(len(valid_triangles))


if __name__ == '__main__':
    main()
