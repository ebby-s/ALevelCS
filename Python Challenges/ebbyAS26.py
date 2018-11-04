import numpy

def word_length(text):
    punc_list = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    no_punc = ""
    for letter in text:
        if letter not in punc_list:
            no_punc += letter
    text = no_punc.split(" ")
    lengths = []
    for word in text:
        lengths.append(len(word))
    return numpy.mean(lengths)
