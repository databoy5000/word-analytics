# Words-Analytics

## Brief
- Language: Python
- Produce a list of the most frequent interesting words, along with a summary table showing where those words appear (sentences and documents).
- Output: my choice.
- Example: see document Back-end_Coding_Test.docx
- [Repository](https://github.com/databoy5000/word-analytics)

## Tools
- IDE: VS Code
- Language: Python
- Modules:
	- collections (built-in module) - implements specialised container data types.
	- re - regular expressions.
	- pandas
	- nltk.corpus (stopwords)

```py
pip install --user -U nltk
```

## Appendixes
- [How to Clean Text Data](https://towardsdatascience.com/how-to-clean-text-data-639375414a2f)

## Pseudo code
- Loop 1: Iterate through each document...
	- get all words (to count all keywords) - keywords can also be stored as a tuple (keyword, document) in a words list
		- data "keyword" ✅
		- data "document" ✅
		- data "count" ✅
	- get all sentences in a sentences list
- Loop 2: Iterate through words list to build the words dictionary...
	- dict "keyword" ✅
	- dict "document" ✅
	- dict "count" ✅
		- if keyword in words dictionary, add count, document
		- else, add keyword, count, document
	- dict "sentences" ✅
- Transfer data to JSON file

## Main variables
- words list: words = [(str,str),(str,str),...]
  - list of tuples to take advantage of tuple unpacking
  - tuple: (keyword, document)
- sentences list: sentences = [str, str,...]
  - list of strings
- words dictionary: words_data =
```py
[
    {
        "keyword": str,
        "document": {str},
        "count": int,
        "sentences": [str,str,str]
    },
    {...}
]
```
  - "document" as a set of strings to only allow unique values
  - "count" as an integer

## General approach
- Setup the project
- Pseudo code
- Think about possible useful modules/tools to setup on the project
- Built/Test/Debug small components
- Bring bring smaller components together and test/debug
- Separate functions into packages
- Deliver
- Look on possible improvements

## Personal comments
My initial pseudo code was a bit too detailed, missing some data types and wasn't focused enough on control flow which led to major pitfalls and having to re-pseudo code the larger component, leading to re-writing the logic from the ground up.

## Improvements
See comments in code.