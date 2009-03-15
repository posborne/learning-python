#!/usr/bin/env python

######################################################################
# Part VIII - Chapter 27 exercise 2
#####################################################################

class FileWrapper(object):
    """
    This class takes a filename and reads the data 
    in the file as text. It provides functions for 
    getting at the data in the file.  It is worth
    noting that all data read is upfront, so access
    after construction will be fast but it consumes
    memory (so limit the number of wrappers initialized).
    """
    def __init__(self, filename):
        file = open(filename)
        text = file.read()
        self.paragraphs = text.split('\n\n')
        self.lines = text.split('\n')
        self.words = []
        for line in self.lines:
            for word in line.split(' '):
                self.words.append(word)

    def word(self, index):
        return self.words[index]

    def line(self, index):
        return self.lines[index]

    def paragraph(self, index):
        return self.paragraphs[index]


if __name__ == '__main__':
    f = FileWrapper('pepper.txt')
    print "First Paragraph"
    print f.paragraph(0), "\n"
    
    print "Third Paragraph"
    print f.paragraph(2), "\n"

    print "Seventh Line"
    print f.line(6), "\n"

    print "66th word:", f.word(65) # haha, f.word

    print "third to last word:", f.word(-3)
