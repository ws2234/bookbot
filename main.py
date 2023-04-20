def count_words(contents):
    words = contents.split()
    print(len(words))

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)

count_words(file_contents)