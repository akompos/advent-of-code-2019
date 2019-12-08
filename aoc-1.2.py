import pytest
from typing import List






def compute(s: str) -> int:
    running_sum = 0
    for module in s.splitlines():
        mass = int(module)

        fuel = mass // 3 - 2
        running_sum += fuel

        while (fuel // 3 - 2) > 0:
            fuel = fuel // 3 - 2
            running_sum += fuel
    return running_sum


def test(input_l: List[int], expected: int) -> None:
    assert compute(input_l, ) == expected

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('14', 2),
        ('1969', 966),
        ('100756', 50346),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:

    with open('inputs/aoc-1.txt', 'r') as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':

    exit(main())
