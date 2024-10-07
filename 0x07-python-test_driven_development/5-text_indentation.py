#!/usr/bin/python3
'''
    this module contains function text_indentation
    if text is not a string, raise a TypeError
'''


def text_indentation(text):
    '''
        this function indents a text using various specifiers
        Args:
            text - the text to be indented
    '''

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in [".", "?", ":"]:
            print(text[i])
            print()
            i += 1
        else:
            print(text[i], end="")
        i += 1
