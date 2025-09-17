# Import sys module to access command-line arguments
import sys

# Import functions from the stats.py module
from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)

# Main function: this is the entry point of the program
def main():
     # Check if the user provided a command-line argument for the book file path
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit the program if no argument was provided
    
    # Get the book path from the first command-line argument
    book_path = sys.argv[1]

    # Read the book's text from the file
    text = get_book_text(book_path)

    # Count the total number of words in the text
    num_words = get_num_words(text)

    # Create a dictionary counting how many times each character appears
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    # Print a report summarizing the results
    print_report(book_path, num_words, chars_sorted_list)

# Function to read the entire contents of a file
def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # Loop over each character in the sorted list
    for item in chars_sorted_list:
        if not item["char"].isalpha(): # Skip non-alphabetic characters
            continue
        # Print character and its frequency
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

# Run the main function when the script is executed
main()
