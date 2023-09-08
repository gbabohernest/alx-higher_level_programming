#!/usr/bin/python3
"""Define a function that prints indented text"""


def text_indentation(text):
    """Prints a text with 2 new lines
       after each ".?:" characters.

    arg:
        text - a string of texts
    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentences = []
    sentence = ""

    for char in text:
        sentence += char
        if char in ".?:":
            sentence = sentence.strip()
            sentences.append(sentence)
            sentence = ""

    if sentence:
        # handle the last sentence
        sentences.append(sentence.strip())

    for sentence in sentences:
        print(sentence)
        print()
