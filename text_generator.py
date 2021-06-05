from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
import random
import re


def find_next_word(word, dict_of_freq):  # function to first five words
    next_word = random.choices(list(dict_of_freq[word].keys()), weights=list(dict_of_freq[word].values()))[0]
    while re.match(".+[^.?!]$", next_word) is None:
        infinite_check = next_word
        next_word = random.choices(list(dict_of_freq[word].keys()), weights=list(dict_of_freq[word].values()))[0]
        if next_word == infinite_check:  # check if loop is not infinite - there is no match
            return
    return next_word


def generate_first_word(dict_of_freq):
    word = random.choice(list(dict_of_freq.keys()))
    while re.match("[A-Z].+[^.?!] .+[^.?!]$", word) is None:
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
    while True:
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
    tk = WhitespaceTokenizer()
    corpus_file = open(input(), 'r', encoding='utf-8')
    list_of_tokens = tk.tokenize(corpus_file.read())
    dict_of_bigrams = {}

    for curr_head_idx, head in enumerate(list_of_tokens):
        curr_head = head + ' ' + list_of_tokens[curr_head_idx+1]
        if curr_head_idx == len(list_of_tokens)-3:  # last element in list isn't a head
            break
        elif dict_of_bigrams.setdefault(curr_head):  # check if key(token) already exists in dict
            dict_of_bigrams[curr_head].append(list_of_tokens[curr_head_idx+2])
        else:  # add new kew to dict
            dict_of_bigrams[curr_head] = [list_of_tokens[curr_head_idx+2]]

    for key, val in dict_of_bigrams.items():
        frq_counter = Counter(val)
        dict_of_bigrams[key] = frq_counter

    i = 0
    while i < 10:
        if generate_sentence(dict_of_bigrams):
            i += 1



if __name__ == "__main__":
    main()
