'''
Python functions to be used as command-line tools:

    $ project_name Hello World
    Hello World

http://python-packaging.readthedocs.org/en/latest/command-line-scripts.html#the-console-scripts-entry-point
'''
import sys


def main():
    print('%s %s' % (sys.argv[1], sys.argv[2]))
