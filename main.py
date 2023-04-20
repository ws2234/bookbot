def read_file_contents(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def get_word_counts(contents):
    words = contents.split()
    return len(words)

def get_letter_counts(contents):
    letter_counts = {}

    words = contents.split()
    for word in words:
        for letter in word:
            if letter.lower() in letter_counts:
                letter_counts[letter.lower()] += 1
            else:
                letter_counts[letter.lower()] = 1

    return letter_counts

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
def print_sorted_list(sorted_list):
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

def main():
    file_path = "books/frankenstein.txt"
    print(f"--- Begin report of {file_path} ---")
    file_contents = read_file_contents(file_path)
    word_count = get_word_counts(file_contents)
    letter_counts = get_letter_counts(file_contents)
    print(f"{word_count} words found in the document")
    sorted_char_list = chars_dict_to_sorted_list(letter_counts)
    print_sorted_list(sorted_char_list)
    print("--- End report ---")

main()