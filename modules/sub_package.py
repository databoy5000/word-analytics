import re
import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords


def filter_words_by_len(words,word_len=1):
    return list(filter(lambda word: len(word) > word_len, words))


def sanitise_words(words):

    stop_words = stopwords.words('english')

    return [word for word in words if word not in stop_words]


def build_words_list(string, doc_title):

    lower_case_txt = string.lower()
    doc_words_raw = re.split(r'[\n+\s+\W+\d+]', lower_case_txt)

    # ? I expected 'None' (or empty string, list, dict, etc) to be falsey. Why does None == False return False?
    doc_words_noempty = list(filter(None, doc_words_raw))

    # ? Here, is it ok instead to just re-assign 'doc_words' multiple times (perhaps just adding comments as explanation instead) or better practice to change variable to name (with no comments)?
    doc_words_noshort = filter_words_by_len(doc_words_noempty)
    doc_words_sanitised = sanitise_words(doc_words_noshort)
    
    return [(word,doc_title) for word in doc_words_sanitised]


def build_sentences_list(string):
    
    # ? I was unable to remove the line break directly with the pattern. What is the better way?
    line_sentences = re.split(r'(?<=[.!?])([\s+])',string)
    line_sentences_noempty = list(filter(None, line_sentences))

    for item in line_sentences_noempty:
        # ? why (item != None) does not work in a single IF statement (chained with 'or')?
        if (item == None) or (item == ' ') or (item == '\n'):
            continue
        else: 
            return item


def get_sentences(all_sentences, keyword):
    
    selected_sentences = list()
    
    for sentence in all_sentences:
#         ? Why does the first sentence iteration match with the keyword, but doesn't on next iterations?
#         is_keyword_match = re.match(rf'\b{re.escape(keyword)}\b',sentence.lower())

        word_matches = re.findall(rf'\b{re.escape(keyword)}\b',sentence.lower())

        if len(word_matches) > 0:
            selected_sentences.append(sentence)
            
    return selected_sentences


def build_word_dictionary(keyword, document, sentences, added_keywords):
    
    # ? Is there anything wrong with using the same word for an arg in a function + a variable name (e.g. sentences, keyword)
    selected_sentences = get_sentences(sentences, keyword)

    new_word_dict = {
        'keyword': keyword,
        'documents': {document},
        'count': 1,
        'sentences': selected_sentences,
    }

    added_keywords.add(keyword)

    return new_word_dict.copy()