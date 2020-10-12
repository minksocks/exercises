"""Generate bar chart"""
import sys
import pprint
import string
from collections import defaultdict

text = 'Heads up, playing for keeps. You can\'t teach an old dog new tricks. Elephant in the room, it\'s not all it\'s cracked up to be.'

def main():
    """Takes sentance input as string. Prints out a "bar chart" which counts occurance of each letter."""
    mapped = defaultdict(list)
    for character in text:
        character = character.lower()
        if character in string.ascii_lowercase[:]:
           mapped[character].append(character) 
    
    print("\nThe following is the text to be bar charted:\n")
    print("text = ", end='')
    print("{}\n".format(text), file=sys.stderr)
    pprint.pprint(mapped, width=110)


if __name__ == "__main__":
    main()
