#!/usr/bin/python3

def multiple_returns(sentence):

    if sentence is not None and len(sentence) > 0:
        length = len(sentence)
        result = (length, sentence[0])
        return result
    else:
        return (len(sentence), None)
