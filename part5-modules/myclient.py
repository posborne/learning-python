from mypkg import *

if __name__ == '__main__':
    filename = raw_input("Input a filename: ")
    print "countLines:", countLines(filename)
    print "countChars:", countChars(filename)
    print "test: ", test(filename)
