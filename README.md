# A-Word-Frequency-Thing
## Intro
The program can be run via the command line, and a nice table is printed of the results. But since the size of the terminal is limited, a Flask server is available to serve the data to the browser so as to be printed in an even nicer table.

### Running the program
First, enter the `venv`:
```
. env/bin/activate
```
Run the program in the browser (recommended):
```
export FLASK_APP=app
flask run 
```
Run the program in the CLI:
```
python word_finder.py
```
## Code walkthrough

### get_data() - the main algorithm
1) It loops through each document in `test_docs`
2) It splits the text up into sentences
3) For each split sentence, it checks that the text is not empty (it ignores it if so) before cleaning up each sentence
3.1 see *sentence_data()* for more information
3.2 Note: the a copy of each sentence has its whitespace removed, and they are stored separetly in `sentence` for later use when adding to the dictionary
4) Each word is then compared to the dictionary
4.1 If the word does not exist in the dictionary, a new entry is made in the name of the word
4.2 Each attribute in the entry is then updated accordingly: a counter, a list of locations the word exists in, and a list of sentences that the word is used in
5) Finally, the dictionary is returned

### filter_data()
Given a dictionary of data returned from `get_data()`, a new filtered dictionary is created. Here is responsbile for deciding what makes a word "interesting" (as asked for in the challenge specification). Essentially, a word is "interesting" if it's at least *x* large and occurs at least *y* number of times.

1) Each entry in the dictionary is filtered by its `counter` value and by the literal size of the word
1.1 If specific conditions are met, the word is added to the filtered list and returned

### sentence_cleaner()
Here, each sentence is "cleaned": all punctuation is removed, then the text's case is lowered and split. This is what allows the words to be read easily.

### table_results()
A simple function to print the results in a table in the CLI.