import typing


def compute(s: str) -> int:
    beg_s, end_s = s.strip().split('-')
    beg, end = int(beg_s), int(end_s)
    n = 0
    for i in range(beg, end):
        str_i = str(i)
        if len(str_i) != 6:
            continue
        if not (
            ord(str_i[0]) <= ord(str_i[1]) <= ord(str_i[2]) <=
            ord(str_i[3]) <= ord(str_i[4]) <= ord(str_i[5])
        ):
            continue
        adjacent_same = False
        prev = str_i[0]
        for c in str_i[1:]:
            if c == prev:
                adjacent_same = True
            prev = c
        if not adjacent_same:
            continue

        n += 1

    return n


def main() -> int:

    with open('inputs/aoc-4.txt', 'r') as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())

