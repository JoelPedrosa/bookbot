from stats import word_count, caracter_count, sorted_dict
import sys

def get_book_text(pathfile) :
    with open(pathfile) as f:
        book_content = f.read()
    return book_content
        

def main() :
    if len(sys.argv) == 2:
     print("============ BOOKBOT ============")
     print(f"Analyzing book found at {sys.argv[1]}")
     print("----------- Word Count ----------")
     print(f"Found {word_count(get_book_text(sys.argv[1]))} total words")
     print("--------- Character Count -------")
     sorted_chars = sorted_dict(caracter_count(get_book_text(sys.argv[1])))
     for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"{char}: {count}")
    elif len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
