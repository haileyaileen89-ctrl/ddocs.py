# Author: [Aileen Odwori]
# Date: 20 March 2026
# Description: Program to perform string reversal using two methods
#              and character frequency analysis with sorting and case sensitivity options.

def reverse_string_slicing(hello, world):
    """Reverse string using slicing [::-1]"""
    return hello, world[::-1]

def reverse_string_loop(hello, world):
    """Reverse string using a loop and concanetation"""
    reversed_str = ""
    for char in hello, world:
        reversed_str = char + reversed_str  
    return reversed_str

def character_frequency(user_input, case_sensitive=True, sort_by="char"):
    """Count frequency of each character and return sorted results"""
    if not case_sensitive:
        user_input = user_input.lower()

    freq_dict = {}
    for char in user_input:
        freq_dict[char] = freq_dict.get(char, 0) + 1

    # Sorting logic
    if sort_by == "char":
        sorted_items = sorted(freq_dict.items(), key=lambda x: x[0])
    elif sort_by == "freq":
        sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    else:
        sorted_items = freq_dict.items()

    return sorted_items, len(user_input), len(freq_dict)

def main():
    
    user_input = input("Enter a string: ")

    print("=== STRING REVERSAL ===")
    print("Method 1 (Slicing):", reverse_string_slicing(user_input))
    print("Method 2 (Loop):", reverse_string_loop(user_input))

    print("=== CHARACTER FREQUENCY ===")
    # Case sensitivity option
    case_sensitive = True  
    sort_by = "char"       

    freq_results, total_chars, unique_chars = character_frequency(user_input, case_sensitive, sort_by)

    
    print("Character | Count")
    print("-----------------")
    for char, count in freq_results:
        print(f"'{char}' | {count}")
    print("Total characters:", total_chars)
    print("Unique characters:", unique_chars)