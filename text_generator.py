from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
import random

PUNCTUATION_MARKS = '.?!'


def find_next_word(word, dict_of_freq):
    return random.choices(list(dict_of_freq[word].keys()), weights=list(dict_of_freq[word].values()))[0]


def generate_first_word(dict_of_freq):
    while True:
        word = random.choice(list(dict_of_freq.keys()))
        if word[0].isupper() and word[-1] not in PUNCTUATION_MARKS:
            return word


def generate_sentence(dict_of_freq):
    curr_word = generate_first_word(dict_of_freq)
    for curr_word_idx in range(5):
        if curr_word[-1] in PUNCTUATION_MARKS:
            print(curr_word[:-1], end=' ')
        else:
            print(curr_word, end=' ')
        curr_word = find_next_word(curr_word, dict_of_freq)

    while True:
        curr_word = find_next_word(curr_word, dict_of_freq)
        if curr_word[-1] in PUNCTUATION_MARKS:
            print(curr_word, end='\n')
            break
        else:
            print(curr_word, end=' ')


def main():
    tk = WhitespaceTokenizer()
    corpus_file = open(input(), 'r', encoding='utf-8')
    list_of_tokens = tk.tokenize(corpus_file.read())
    dict_of_bigrams = {}

    for curr_head_idx, head in enumerate(list_of_tokens):
        if curr_head_idx == len(list_of_tokens)-1:  # last element in list isn't a head
            pass
        elif dict_of_bigrams.setdefault(head):  # check if key(token) already exists in dict
            dict_of_bigrams[head].append(list_of_tokens[curr_head_idx+1])
        else:  # add new kew to dict
            dict_of_bigrams[head] = [list_of_tokens[curr_head_idx+1]]

    for key, val in dict_of_bigrams.items():
        frq_counter = Counter(val)
        dict_of_bigrams[key] = frq_counter

    for curr_sentence_idx in range(10):
        generate_sentence(dict_of_bigrams)


if __name__ == "__main__":
    main()
