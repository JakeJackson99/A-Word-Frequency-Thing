"""
TODO
1) Read each file
2) For each file, split the text up into sentences (i.e. .split("."))
    2.1) Before reading the split text, remove the punctuation and lower the word's case
3) Identify "interesting" words (decide what that means later)
4) If the word is in the dictionary, increment the key's "counter" value; else add it to the dict
   along with the file name it occurs in and the sentence itself WITH the punction.

NOTE
- Only add a word's location if it hasn't already been added (cannot use sets in dictionaries)

Format:
words = {
    word: {
        counter: int,
        files: [str],
        sentences: [str]
    }
}
"""

