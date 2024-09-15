from itertools import permutations
def solve_cryptarithmetic(word1, word2, word3):
    unique_letters = set(word1 + word2 + word3)
    if len(unique_letters) > 10:
        print("Error: Too many unique letters for a valid solution.")
        return None
    for values in permutations(range(10), len(unique_letters)):
        letter_to_digit = dict(zip(unique_letters, values))
        if letter_to_digit[word1[0]] == 0 or letter_to_digit[word2[0]] == 0 or letter_to_digit[word3[0]] == 0:
            continue
        num1 = int(''.join(str(letter_to_digit[letter]) for letter in word1))
        num2 = int(''.join(str(letter_to_digit[letter]) for letter in word2))
        num3 = int(''.join(str(letter_to_digit[letter]) for letter in word3))
        if num1 + num2 == num3:
            return num1, num2, num3, letter_to_digit
    return None
word1 = input("Enter the first word: ").upper()
word2 = input("Enter the second word: ").upper()
word3 = input("Enter the third word: ").upper()
result = solve_cryptarithmetic(word1, word2, word3)
if result:
    num1, num2, num3, letter_to_digit = result
    print(f"{word1} = {num1}, {word2} = {num2}, {word3} = {num3}")
    print("Letter to Digit Mapping:", letter_to_digit)
else:
    print("No solution found.")
