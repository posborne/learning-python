#!/usr/bin/env python

def countLines(filename):
    """
    Count the number of lines in the specified file
    """
    return len(file(filename).readlines())

def countChars(filename):
    """
    Count the number of characters in the specified file
    """
    chars = 0
    for line in file(filename).readlines():
        chars += len(line)
    return chars
    
def test(filename):
    """
    Count the lines and numbers of characters in the specified file.
    This returns a tuple in the form (lines, characters) for the
    file.
    """
    # this could be optimized to only open the file once
    return (countLines(filename), countChars(filename))


if __name__ == '__main__':
    filename = raw_input('Enter filename: ')
    res = test(filename)
    print "The file \"%s\" has %i lines and %i characters" % (filename, res[0], res[1])
