from nltk.tokenize import WhitespaceTokenizer
import sys


def main():
    tk = WhitespaceTokenizer()
    corpus_file = open(input(), 'r', encoding='utf-8')
    list_of_tokens = tk.tokenize(corpus_file.read())
    list_of_bigrams = []
    for i, token in enumerate(list_of_tokens):
        if i == len(list_of_tokens)-1:
            pass
        else:
            bigram = [token, list_of_tokens[i+1]]
            list_of_bigrams.append(bigram)

    print(f'Number of bigrams: {len(list_of_bigrams)}')
    while True:
        try:
            idx = input()
            if idx == 'exit':
                break
            else:
                print(f'Head: {list_of_bigrams[int(idx)][0]}    Tail: {list_of_bigrams[int(idx)][1]}')
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
        except ValueError:
            print('Type Error. Please input an integer.')


if __name__ == "__main__":
    main()
