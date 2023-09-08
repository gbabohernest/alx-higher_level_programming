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

    sentence = ""

    for char in text:
        sentence += char
        if char in ".?:":
            while sentence[0] == " ":
                sentence = sentence[1:]
            print(sentence)
            print()
            sentence = ""

    if len(sentence) != 0:
        # handle the last sentence
        try:
            while sentence[0] == " ":
                sentence = sentence[1:]
        except Exception:
            pass
        print(sentence, end="")
