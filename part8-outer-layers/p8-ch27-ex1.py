#!/usr/bin/env python

######################################################################
# This python module is a replacement of the pepper.py
# example from the text but without the use of regular
# expressions:  The original program was as follows:
#
# import re
# file = open('pepper.txt')
# text = file.read()
# paragraphs = text.split('\n\n')
# matchstr = re.compile(
#     r"""\b(red|green)
#         (\s+
#          pepper
#          (?!corn)
#          (?=.*salad))""",
#        re.IGNORECASE |
#        re.DOTALL
#        re.VERBOSE)
# for paragraph in paragraphs:
#     fixed_paragraph = matchstr.sub(r'bell\2', paragraph)
#     print fixed_paragraph + '\n'
######################################################################
    
def pepperCond(word):
    """
    Return true if the word is some form of pepper and
    false if not
    """
    try:
        word.lower().index('pepper')
    except:
        return False
    return True

def cornCond(word):
    """
    Return false if the word is corn and false if not
    """
    try:
        word.lower().index('corn')
    except:
        return True
    return False

def saladCond(words):
    """
    Do a linear search for salad in words.  Return true
    if words contains a form of salad and false if not
    """
    for word in words:
        try:
            word.lower().index('salad')
            return True
        except:
            continue
    return False

if __name__ == '__main__':
    import string

    file = open('pepper.txt')
    text = file.read()
    paragraphs = text.split('\n\n')

    for paragraph in paragraphs:
        lines = paragraph.split('\n')
        t = string.join(lines, ' ')
        words = t.split(' ')
        for i in range (len(words) - 3):
            if pepperCond(words[i]) and cornCond(words[i]) and saladCond(words[i:]):
                print paragraph + '\n'
                break
