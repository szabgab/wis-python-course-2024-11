text = "12874681🐍7 481٣"

# Count the number of digits in the text
count = 0
for char in text:
    if char.isdigit():
        count += 1
        print(count)
print(f"Number of digits in the text: {count}")
print(len(text))


# Count how many times each digit appears in the text
number_of_digit = [0] * 10
print(number_of_digit)
for char in text:
    if char.isdigit():
        number_of_digit[int(char)] += 1
print(number_of_digit)
# for i, count in enumerate(digits):
#     print(f"{i}: {count}")


# for count in digits:
#     print(count)

for i in range(10):
    print(f"{i}: {number_of_digit[i]}")