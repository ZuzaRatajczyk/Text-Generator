from nltk.tokenize import WhitespaceTokenizer
import sys


def main():
    tk = WhitespaceTokenizer()
    corpus_file = open(input(), 'r', encoding='utf-8')
    list_of_tokens = tk.tokenize(corpus_file.read())
    print('Corpus statistics')
    print(len(list_of_tokens))
    print(len(set(list_of_tokens)))
    while True:
        try:
            idx = input()
            if idx == 'exit':
                break
            else:
                print(list_of_tokens[int(idx)])
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
        except ValueError:
            print('Type Error. Please input an integer.')



if __name__ == "__main__":
    main()
