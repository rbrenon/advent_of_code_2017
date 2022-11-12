

def main():
    with open("input.txt") as f:
        raw_input = f.readlines()
    # input_data = [data.split("\t") for data in raw_input]
    part_one(raw_input)


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


if __name__ == "__main__":
    main()