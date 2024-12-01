# filename = "day05/digits.txt"
# filename = input("Enter the filename: ")
import sys

def count_digits(text):
    number_of_digit = [0] * 10
    for char in text:
        if char.isdigit():
            if char == "2":
                continue
            number_of_digit[int(char)] += 1
    return number_of_digit


def get_input():
    print(sys.argv)
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")

    print(sys.argv[1])
    filename = sys.argv[1]

    with open(filename, "r") as fh:
        text = fh.read()
    return text

def print_table(number_of_digit):
    for i, count in enumerate(number_of_digit):
        print(f"{i}: {count}")

if __name__ == "__main__":
    text = get_input()
    number_of_digit = count_digits(text)
    print_table(number_of_digit)
