def main():
    book_path = "/Users/joshuataylor/workspace/github.com/Abstrxxxct/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    
    num_words = count_words(text)
    char_count = count_characters(text)
    
    print_report(book_path, num_words, char_count)

def get_book_text(path):
    with open(path, "r") as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():  # Only count alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def print_report(book_path, num_words, char_count):
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

if __name__ == "__main__":
    main()
