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
        string = re.sub('(?<=[?,!.:–"\\s#])' + word + '(?=[?,!.:–"\\s#])', initial, string, flags=re.IGNORECASE)
    return string


word_file = open('words.txt', 'r')

word_dict = get_word_dict_from_file(word_file)

print(replace_words_from_dict(word_dict, "Let me get this straight: Democrats and the mainstream media are trying to incite panic over the Coronavirus ...Yet they still push an open border agenda that allows thousands of unchecked & potentially unhealthy migrants to flow into America?"))
