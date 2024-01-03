def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    letter_count = count_letters(text)
    print ("Here is a sweet report on frankenstein.txt")
    print(f"{num_words} words found in the document")
    for key, value in letter_count.items():
        print (f'The letter {key} appears {value} times')

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lowercase_text = text.lower()
    letters_in_alpha = ["a","b",'c','d','e','f','g','h','i','j',
                        'k','l','m','n','o','p','q','r','s','t',
                        'u','v','w','x','y','z']
    letter_count_dict = {}
    for letter in letters_in_alpha:
        letter_count_dict[letter] = lowercase_text.count(letter)
    return letter_count_dict


main()