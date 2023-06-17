from collections import Counter

word = input("Give me a word: ")

def count_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    counter = Counter(word)
    sum = 0
    for key, item in counter.items():
        if key in vowels:
            sum += item

    return sum

print(count_vowel(word))

