#!/usr/bin/python3
def multiple_returns(sentence):
    """ Commands to make it equal None """
    if len(sentence) == 0:
        return (0, "None")
    return (len(sentence), sentence[0])
