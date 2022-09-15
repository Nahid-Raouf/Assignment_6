import string
my_sentence = "today is rainy"
def count_word_string(sentence):
 num_words = sum([i.stript(string.punctuation).isalpha() for i in sentence.split()])
 return num_words

print("Orginal sentence :", my_sentence)
print("number of wors=ds in original sentence : ", count_word_string(my_sentence))
