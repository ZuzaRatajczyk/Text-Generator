from nltk.tokenize import WhitespaceTokenizer
from collections import Counter
import sys


def main():
    tk = WhitespaceTokenizer()
    print("Enter corpus file:")
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

    while True:
        try:
            input_head = input()
            if input_head == 'exit':
                break
            else:
                if dict_of_bigrams.setdefault(input_head):
                    print(f"Head: {input_head}")
                    for key, val in dict_of_bigrams[input_head].items():
                        print(f"Tail: {key} Count: {val}")
                else:
                    print("The requested word is not in the model. Please input another word.")
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
        except ValueError:
            print('Type Error. Please input an integer.')


if __name__ == "__main__":
    main()
