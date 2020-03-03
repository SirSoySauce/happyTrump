import re


def get_word_dict_from_file(file):
    word_dict = {}
    lines = file.readlines()
    for line in lines:
        split_word = line.strip().split(':')
        word_dict[split_word[0]] = split_word[1]
    return word_dict


def replace_words_from_dict(dict, string):
    for word, initial in dict.items():
        string = re.sub(" " + word, " " + initial, string, flags=re.IGNORECASE)
    return string


word_file = open('words.txt', 'r')

word_dict = get_word_dict_from_file(word_file)

print(replace_words_from_dict(word_dict,
                              "This is an incredible time for our nation—we are in the midst of the Great American Comeback! Jobs are booming, incomes are soaring, poverty is plummeting, confidence is surging, and we have completely rebuilt the awesome power of the U.S. Military. PROMISES MADE, PROMISES KEPT!"))
