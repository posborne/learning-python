#!/usr/bin/env python

import os, sys

class MyPrompt:
    """
    This is a modified version of the python interactive prompt
    which displays more than the simple >>>
    
    The default displays the following:
    /path/to/cwd| 27 >>>
    
    where 27 is the current line (command executed) number.
    """
    
    def __init__(self, subprompt='>>> '):
        self.lineNumber = 0
        self.subprompt = subprompt

    def __repr__(self):
        self.lineNumber += 1
        return os.getcwd() + '|%d %s' % (self.lineNumber, self.subprompt)

# To use import this module from the interactive prompt
sys.ps1 = MyPrompt(">>> ")
