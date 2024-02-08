text = "hire employees"

def reverseText(text):
    n = len(text)
    print("\nReversed Text:")
    for i in range(n):
        print(text[n - i - 1], end="")

def textAnalyzer(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count_words = 1
    count_letters = 0
    count_vowels = 0
    count_consonants = 0
    for char in text:
        if char.isalpha():
            count_letters += 1
            if char.lower() in vowels:
                count_vowels += 1
            else:
                count_consonants += 1
        elif char == ' ':
            count_words += 1
    print("Words in the Text:", count_words)
    print("Letters in the Text:", count_letters)
    print("Vowels in the Text:", count_vowels)
    print("Consonants in the Text:", count_consonants)
    reverseText(text)

textAnalyzer(text)
