from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
import random
import re


def create_dict_of_trigrams(file):
    tk = WhitespaceTokenizer()
    list_of_tokens = tk.tokenize(file.read())
    dict_of_trigrams = {}

    for curr_head_idx, head in enumerate(list_of_tokens):
        curr_head = head + ' ' + list_of_tokens[curr_head_idx+1]
        if curr_head_idx == len(list_of_tokens)-3:  # last two elements in list isn't a head
            break
        elif dict_of_trigrams.setdefault(curr_head):  # check if key(token) already exists in dict
            dict_of_trigrams[curr_head].append(list_of_tokens[curr_head_idx+2])
        else:  # add new kew to dict
            dict_of_trigrams[curr_head] = [list_of_tokens[curr_head_idx+2]]

    for key, val in dict_of_trigrams.items():
        frq_counter = Counter(val)
        dict_of_trigrams[key] = frq_counter

    return dict_of_trigrams


def find_next_word(word, dict_of_freq):  # function to first five words
    next_word = random.choices(list(dict_of_freq[word].keys()), weights=list(dict_of_freq[word].values()))[0]

    while re.match(".+[^.?!]$", next_word) is None:
        repetition_check = next_word
        next_word = random.choices(list(dict_of_freq[word].keys()), weights=list(dict_of_freq[word].values()))[0]
        if next_word == repetition_check:  # check if generated word is the same - if true try to generate new sentence
            return

    return next_word


def generate_first_word(dict_of_freq):
    word = random.choice(list(dict_of_freq.keys()))

    while re.match("[A-Z].+[^.?!] .+[^.?!]$", word) is None:  # start with capitalized words and
        # not start with a word that ends with a sentence-ending punctuation mark
        word = random.choice(list(dict_of_freq.keys()))

    return word


def generate_sentence(dict_of_freq):
    generation_successful = True
    sentence = []
    curr_word = generate_first_word(dict_of_freq)
    sentence.append(curr_word.split()[0])

    for curr_word_idx in range(4):  # sentence must has min. 5 words
        previous_word = curr_word.split()[1]
        next_word = find_next_word(curr_word, dict_of_freq)
        if next_word:
            curr_word = previous_word + ' ' + next_word
            sentence.append(curr_word.split()[0])
        else:
            generation_successful = False
            return generation_successful  # can't generate sentence with min. 5 words and try again

    while True:  # while word don't end with '.' or '?' or '!'
        if re.match(".+[.?!]$", curr_word):
            sentence.append(curr_word.split()[1])
            break
        else:
            previous_word = curr_word.split()[1]
            curr_word = previous_word + ' ' + random.choices(list(dict_of_freq[curr_word].keys()),
                                                             weights=list(dict_of_freq[curr_word].values()))[0]
            sentence.append(curr_word.split()[0])

    print(" ".join(sentence))
    return generation_successful


def main():
    corpus_file = open(input(), 'r', encoding='utf-8')
    dict_of_trigrams = create_dict_of_trigrams(corpus_file)
    i = 0
    while i < 10:  # generate ten sentences
        if generate_sentence(dict_of_trigrams):
            i += 1


if __name__ == "__main__":
    main()
