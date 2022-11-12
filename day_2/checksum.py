from itertools import permutations


def main():
    with open("input.txt") as f:
        raw_input = f.readlines()
    # input_data = [data.split("\t") for data in raw_input]
    part_one(raw_input)
    part_two(raw_input)


def part_one(input_data: list[str]) -> None:
    """
    The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right
    track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the
    largest value and the smallest value; the checksum is the sum of all of these differences.
    :param input_data:
    :return:
    """
    checksum = 0

    for line in input_data:
        numbs = [int(numb) for numb in line.split("\t")]
        checksum += max(numbs) - min(numbs)

    print(f"part 1: {checksum}")    # 30994


def part_two(data: list[str]):
    """
    the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result
    of the division operation is a whole number. They would like you to find those numbers on each line, divide them,
    and add up each line's result.
    :param data:
    :return:
    """
    checksum = 0

    for line in data:
        numbs: list[int] = [int(numb) for numb in line.split("\t")]

        perms = list(permutations(numbs, 2))
        for perm in perms:
            if perm[0] % perm[1] == 0:
                checksum += (perm[0]//perm[1])
                break

    print(f"part 2: {checksum}")  # high 38082, 26023; 233


if __name__ == "__main__":
    main()