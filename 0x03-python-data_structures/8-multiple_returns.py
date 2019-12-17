#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = ''
    if not sentence.strip():
        first_char = None
    else:
        return len(sentence), sentence[0]
