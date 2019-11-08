import re

# import nltk
# # nltk.download('words')
# from nltk.corpus import words


def OS_textbook_tokenizer(input_filename):
    textbook_word_list = []
    with open(input_filename) as input_file:
        for i in input_file:
            tokenized_line_buffer = re.findall("[\w']+", i)
            tokenized_line_buffer = set([i.lower() for i in tokenized_line_buffer if len(i) != 1])
            textbook_word_list.extend(tokenized_line_buffer)
    textbook_word_list = set(textbook_word_list)
    return textbook_word_list

def drop_non_english_word(raw_word_list):
    output = [i for i in raw_word_list if i in set(words.words())]
    return output


# a = drop_non_english_word(OS_textbook_tokenizer('textbook.txt'))

# a = OS_textbook_tokenizer('textbook.txt')
# print(a)
