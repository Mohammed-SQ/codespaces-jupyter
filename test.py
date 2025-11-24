
numbers = []
letters = []

while True:
    s = input("Enter something (or type 'Exit' to stop): ").strip()
    if s.lower() == 'exit':
        break

    # build lists of digit characters and letter characters
    digit_chars = []
    letter_chars = []
    for ch in s:
        if ch.isdigit():
            digit_chars.append(ch)
        elif ch.isalpha():
            letter_chars.append(ch)

    # number: join digits or store 0 if none
    if len(digit_chars) == 0:
        numbers.append(0)
    else:
        num = int(''.join(digit_chars))
        numbers.append(num)

    # characters: join letters or store '-'
    if len(letter_chars) == 0:
        letters.append('-')
    else:
        letters.append(''.join(letter_chars))

# output
print()
print('Numbers list:', numbers)
print('Characters list:', letters)

total = sum(numbers)
print('Sum of numbers:', total)
if len(numbers) > 0:
    avg = total / len(numbers)
else:
    avg = 0
print(f'Average of numbers: {avg:.2f}')




