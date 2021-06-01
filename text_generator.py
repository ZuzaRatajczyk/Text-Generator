from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
import random


def find_next_word(word, dict_of_freq):
    return random.choices(list(dict_of_freq[word].keys()), weights=list(dict_of_freq[word].values()))[0]


def main():
    tk = WhitespaceTokenizer()
    # print("Enter corpus file:")
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
        curr_word = random.choice(list(dict_of_bigrams.keys()))
        for curr_word_idx in range(10):
            if curr_word_idx == 9:
                print(f'{curr_word}')
            else:
                print(f'{curr_word} ', end='')
            curr_word = find_next_word(curr_word, dict_of_bigrams)


if __name__ == "__main__":
    main()
