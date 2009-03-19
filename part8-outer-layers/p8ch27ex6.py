#!/usr/bin/env python

############################################################
# This is a modified version of mygrep.py that outputs to
# the last file specified instead of stdout.  You should
# really be careful with this.
#
# ex: (search for cows in python files and write to output.txt)
# python p8ch24ex6.py cows *.py output.txt
############################################################

import fileinput, sys
# Take the first argument out of sys.argv[1], sys.argv[2:]
searchterm, sys.argv[1:], outfile = sys.argv[1], sys.argv[2:-1], sys.argv[-1]
f = open(outfile, 'w')
for line in fileinput.input():
    num_matches = line.count(searchterm)
    if num_matches:
        f.write("found '%s' %d times in %s on line %d.\n" % (searchterm, num_matches, fileinput.filename(), fileinput.filelineno()))
f.close()
