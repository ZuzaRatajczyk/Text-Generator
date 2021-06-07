# Text-Generator
This is a project to learn Natural Language Processing. Program is generating pseudo-sentences based on corpus file witch is Game Of Thrones script.

# Trigrams
Corpus (txt file) was transormed into a collection of trigrams. 
Heads consist of two space-separated tokens concatenated into a single string. The tails consist of one token. 
For example: head — winter is, tail — coming.
This is done by function ``` create_dict_of_trigrams()``` witch take opened file as argument.
In this function I've also used ```collections.Counter()``` so result dictonary looks  for example like this: {"winter is": Counter("coming":2}}, witch means that tail "coming" for head "winter is" appears twice in text.

# Generating 10 sentences
Sentences are generated starting from randomly selected head. After that next word are generated randomly taking into account their weight (frequency of occurrence). 



