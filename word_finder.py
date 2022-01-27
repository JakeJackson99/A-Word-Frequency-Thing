from copyreg import constructor
import string
import os


def sentence_cleaner(text):
    """Cleans a given sentence"""

    for char in string.punctuation:
        text = text.replace(char, "")
    return text.lower().split()


def get_data():
    """Reads the files and adds the data to a dictionary"""

    results = {}
    try:
        for filename in os.listdir("test_docss"):
            with open(os.path.join("test_docs", filename)) as file:
                text = file.read().split(".")
                for sentence in text:
                    if sentence == "":
                        continue
                    sentence = sentence.strip()
                    words = sentence_cleaner(sentence)
                    for word in words:
                        if word not in results:
                            results.update({
                                word: {"counter": 0, "documents": [], "sentences": []}})
                        results[word]["counter"] += 1
                        if filename not in results[word]["documents"]:
                            results[word]["documents"].append(filename)
                        if sentence not in results[word]["sentences"]:
                            results[word]["sentences"].append(sentence)
    except FileNotFoundError as e:
        print(e)
    return results


def filter_data(data, freq, word_size):
    """Filters the data

    Args:
        data -- a dictionary of words
        freq -- the minumum frequency for word
        word_size -- the minimum size a word can be (partly to decide how "interesting" it is)
    """

    results = {}
    for key, value in data.items():
        if value["counter"] > freq and len(key) > word_size:
            results.update({key: value})
    return results


def table_results(results):
    """Displays the results in a table via the CLI"""

    print("{:<12} {:<10} {:<60} {:<20}".format(
        "Word", "Frequency", "Documents", "Sentences"))

    for key, value in results.items():
        freq = value["counter"]
        documents = ", ".join(value["documents"])
        sentences = value["sentences"][0]
        print("{:<12} {:<10} {:<60} {:<20}".format(
            key, freq, documents, f"{sentences[0:50]}..."))


if __name__ == "__main__":
    results = filter_data(get_data(), 10, 8)
    table_results(results)
