# sanskritizer/converter.py
from .data import SANSKRIT_DICT

def get_sanskrit_info(word):
    """ Get Sanskrit translation for a given English word """
    word = word.lower()  # Case-insensitive matching
    if word in SANSKRIT_DICT:
        return SANSKRIT_DICT[word]
    else:
        return {"iast": "N/A", "devanagari": "N/A", "pronunciation": "N/A"}

def to_iaST(word):
    """ Convert to IAST format """
    info = get_sanskrit_info(word)
    return info.get("iast", "N/A")

def to_devanagari(word):
    """ Convert to Devanagari script """
    info = get_sanskrit_info(word)
    return info.get("devanagari", "N/A")

def pronunciation(word):
    """ Get pronunciation of the Sanskrit word """
    info = get_sanskrit_info(word)
    return info.get("pronunciation", "N/A")

def user_input():
    """ Allow users to enter a word and return its Sanskrit info """
    word = input("Enter an English word: ").strip().lower()
    
    # Get Sanskrit translation and transliterations
    sanskrit_info = get_sanskrit_info(word)
    
    # Print results
    if sanskrit_info["iast"] != "N/A":
        print(f"Sanskrit (IAST): {sanskrit_info['iast']}")
        print(f"Sanskrit (Devanagari): {sanskrit_info['devanagari']}")
        print(f"Pronunciation: {sanskrit_info['pronunciation']}")
    else:
        print("Sorry, the word is not in the dictionary.")