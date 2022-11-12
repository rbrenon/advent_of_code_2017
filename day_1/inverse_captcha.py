

def main():
    with open("input.txt", "r") as f:
        raw_input = f.readlines()

    input_list = [int(num) for num in raw_input.pop()]

    number_of_elements = len(input_list)

    captcha_sum = 0

    for index, digit in enumerate(input_list):
        if index == number_of_elements - 1:
            if digit == input_list[0]:
                captcha_sum += digit
        elif digit == input_list[index+1]:
            captcha_sum += digit

        print(f"index: {index}, number: {int(digit)}")

    print(f"captcha sum = {captcha_sum}")


if __name__ == "__main__":
    main()