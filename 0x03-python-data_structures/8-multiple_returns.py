#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence.strip():
        return None
    else:
        return len(sentence), sentence[0]
