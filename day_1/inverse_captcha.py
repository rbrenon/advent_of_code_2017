

def main():
    with open("input.txt", "r") as f:
        raw_input = f.readlines()

    input_list = [int(num) for num in raw_input.pop()]
    part_one(input_list)
    part_two(input_list)


def part_one(input_list: list[int]) -> None:
    number_of_elements = len(input_list)
    captcha_sum = 0

    for index, digit in enumerate(input_list):
        if index == number_of_elements - 1:
            if digit == input_list[0]:
                captcha_sum += digit
        elif digit == input_list[index+1]:
            captcha_sum += digit

    print(f"part one: captcha sum = {captcha_sum}") # 995


def part_two(input_list: list[int]) -> None:
    number_of_elements = len(input_list)
    captcha_sum = 0

    for index, digit in enumerate(input_list):
        halfway_digit_index = (index + int(number_of_elements / 2)) % number_of_elements
        halfway_digit = input_list[halfway_digit_index]
        if digit == halfway_digit:
            captcha_sum += digit

    print(f"part twwo: captcha sum = {captcha_sum}") # low 594, 974;  high: 1302


if __name__ == "__main__":
    main()