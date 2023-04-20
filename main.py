def count_words(contents):
    words = contents.split()
    print(len(words))

def count_letters(contents):
    letter_counts = {}

    words = contents.split()
    for word in words:
        for letter in word:
            if letter.lower() in letter_counts:
                letter_counts[letter.lower()] += 1
            else:
                letter_counts[letter.lower()] = 1

    print(letter_counts)

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)

count_words(file_contents)

count_letters(file_contents)