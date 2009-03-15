#!/usr/bin/env python

def describeDirectory(directory, indent=0):
    """
    This function describes a directory structure (recursively)
    starting with the provided directory.  It prints the name
    and size of each file in the directory and recurses into
    subdirectories.
    """
    import os
    
    # Build indent spacing
    indentspace = ''
    for i in range(indent):
        indentspace += '  '

    files = os.listdir(directory) 
    print indentspace, "==", directory, "=="
    for filename in files:
        fullpath = os.path.join(directory, filename)
        try:
            if os.path.isfile(fullpath):
                print indentspace, filename, os.stat(filename).st_size
            elif os.path.isdir(fullpath):
                describeDirectory(fullpath, indent + 1)
        except: pass

if __name__ == '__main__':
    describeDirectory('.')
