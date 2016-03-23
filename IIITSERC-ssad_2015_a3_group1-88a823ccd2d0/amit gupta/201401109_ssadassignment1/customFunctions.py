#!/usr/bin/python
from __future__ import print_function
import os
def clearIt():
	os.system('printf "\033c"')

def printMyBoard(myBoard):
	for x in myBoard:
		for y in x:
			print(y, end='')
		print('')
def clearScreen():
	os.system('printf "\033c"')
	
class attrDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.__dict__ = self
