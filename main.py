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
*- Stripping sentences of their punctuation also strips any necessary apostrophes in words
    - Maybe keep track of the word's index in the sentence BEFORE stripping away the punctuatio
      so it can be added into the 'words' dictionary
- For printing the values, if not being done in the browser, create a table following this guide:
  https://blog.softhints.com/python-print-pretty-table-list/

Format:
words = {
    word: {
        counter: int,
        files: [str],
        sentences: [str]
    }
}
"""
import string


def sentence_cleaner(text):
    for char in string.punctuation:
        text = text.replace(char, "")
    return text.lower().split()

def main():
    results = {}

    for i in range(1, 7):
        with open(f"test_docs/doc{i}.txt") as file:
            text = file.read().split(".")
            for sentence in text:
                if sentence == "":
                    continue
                sentence = sentence.strip()
                words = sentence_cleaner(sentence)
                for word in words:
                    if word not in results:
                        results.update({
                            word: {"counter": 0,
                                   "documents": [], "sentences": []}
                        })

                    results[word]["counter"] += 1
                    if f"doc{i}.txt" not in results[word]["documents"]:
                        results[word]["documents"].append(f"doc{i}.txt")
                    if sentence not in results[word]["sentences"]:
                        results[word]["sentences"].append(sentence)

    for key, value in results.items():
        if 5 < value["counter"] < 8:
            print(key, ' -> ', value)


if __name__ == "__main__":
    main()

    # TESTS
    # for key, value in results.items():
    #     if value["counter"] > 5:
    #         print(key, ' -> ', value)
