#!/usr/bin/env python

############################################################
# This is a basic shell... Note that my implementation is
# very similar to Lutz' because I ended up getting stuck
# and following his code
############################################################

import cmd, os, sys, shutil

class PosixShell(cmd.Cmd):
    """
    This is a simple *nix shell written in python.  It does
    not call system primitives but does them itself.  Currently
    the shell support the following comands:
    ls  << list current directory contents
    cd  << change directory
    mv  << move or rename a file
    cp  << copy a file
  
    At this point glob operations are not supported (e.g. you
    cannot say mv path/to/* ./).
    """    
    
    def do_EOF(self, line):
        """
        On EOF (Ctrl-D) exit
        """
        sys.exit()

    def help_ls(self):
        print "ls <directory>: list the contents of the specified directory"
        print "                (current directory by default)"

    def do_ls(self, line):
        """
        List the current directory
        """
        if line == '': dirs = [os.curdir]
        else: dirs = line.split()
        for dirname in dirs:
            print 'Listing fo %s:' % dirname
            print '\n'.join(os.listdir(dirname))
        
    def do_cd(self, dirname):
        """
        Change to the specified directory.  With no directory
        specified, go to the home directory.
        """
        if dirname == '':
            dirname = os.environ['HOME']
        os.chdir(dirname)

    def do_mkdir(self, dirname):
        """
        Create the specified directory as either an absolutely
        or relatively specified directory
        """
        os.mkdir(dirname)

    def do_cp(self, line):
        """
        Copy source files to destination
        ex:
        cp file1 file2 dest/
        OR
        cp file1 newfile1
        """
        words = line.split()
        sourcefiles, target = words[:-1], words[-1]
        shutil.copy(sourcefile, target)
    
    def do_mv(self, line):
        """
        Move source to target (destroys original file)
        """
        source, target = line.split()
        os.rename(source, target)

    def do_rm(self, line):
        """
        Remove the specified files
        """
        # we can do this as a list comprehension
        [os.remove(arg) for arg in line.split()]

class DirectoryPrompt:
    def __repr__(self):
        return os.getcwd() + '>'

if __name__ == '__main__':
    cmd.PROMPT = DirectoryPrompt()
    shell = PosixShell()
    shell.cmdloop()
