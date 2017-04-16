#!/usr/bin/env python

from machines import OokMachine
import sys
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		raise Exception
	with open(sys.argv[1]) as f:
		program = f.read()
		m = OokMachine()
		m.execute(program)
