# Function to count total number of words in a text
def get_num_words(text):
    words = text.split() # Split the text into words using whitespace
    return len(words) # Return the total number of words

# Function to create a dictionary with the frequency of each character
def get_chars_dict(text):
    chars = {}
    for c in text: # Loop over each character in the text
        lowered = c.lower() # Convert to lowercase so 'A' and 'a' are counted together
        if lowered in chars: # If character already in dictionary
            chars[lowered] += 1 # Increment its count
        else:
            chars[lowered] = 1 # Otherwise, initialize count to 1
    return chars # Return the dictionary

# Helper function to define sorting key for the sorted list
def sort_on(d):
    return d["num"] # Sort by the 'num' key (frequency count

# Function to convert character dictionary to a sorted list of dictionaries
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []

     # Convert dictionary items to a list of dictionaries with keys 'char' and 'num'
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    # Sort the list in descending order based on frequency
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
