
 
from collections import Counter

def sort_string_by_frequency(s):
    # count the frequency of each character
    freq = Counter(s)
    
    # sort the characters by frequency
    sorted_chars = sorted(freq, key=freq.get, reverse=True)
    
    # build the final string by repeating each character by its frequency
    final_str = ''.join(char * freq[char] for char in sorted_chars)
    
    return final_str

