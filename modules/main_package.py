from modules.sub_package import build_words_list
from modules.sub_package import build_sentences_list
from modules.sub_package import build_word_dictionary

def get_data(documents):
    
    words_data = list()
    words = list()
    sentences = list()
    added_keywords = set()

    for doc_title in documents:

        file = open(f'./assets/{doc_title}', 'r')

        for bloc in file:

            # ! Building words list
            words.extend(build_words_list(bloc, doc_title))

            # ! Building sentences list
            sentences.append(build_sentences_list(bloc))

        file.close()

    # ! Building list of keyword dictionaries
    for word_tuple in words:
        keyword,document = word_tuple

        if keyword not in added_keywords:

            word_dict = build_word_dictionary(keyword, document, sentences, added_keywords)

            words_data.append(word_dict)

        else:
            for word_data in words_data:
                if keyword == word_data['keyword']:
                    word_data['count'] += 1
                    word_data['documents'].add(document)
                    break
                    
    for word_dict in words_data:
        word_dict['documents'] = list(word_dict['documents'])
        word_dict['documents'].sort()
        
    return words_data