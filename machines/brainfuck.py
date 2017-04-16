import sys

class Tape:
	
	def __init__(self):
		self.cells = {}
		
	def __getitem__(self, index):
		if not isinstance(index, int):
			raise TypeError
		if index not in self.cells:
			return 0
		return self.cells[index]
		
	def __setitem__(self, index, value):
		if not isinstance(index, int):
			raise TypeError
		self.cells[index] = value

class BrainfuckMachine:
	
	def reset(self):
		self.tape = Tape()
		self.tapePointer = 0
		self.IP = 0
		
	def moveRight(self):
		self.tapePointer += 1
		
	def moveLeft(self):
		self.tapePointer -= 1
		
	def	increment(self):
		self.tape[self.tapePointer] += 1
		
	def decrement(self):
		self.tape[self.tapePointer] -= 1
		
	def output(self):
		print(chr(self.tape[self.tapePointer]), end='')
		
	def input(self):
		self.tape[self.tapePointer] = sys.stdin.read(1)
		
	def loopBegin(self):
		if self.tape[self.tapePointer] == 0:
			level = 1
			self.IP += 1
			while level > 0:
				if self.code[self.IP] == '[':
					level += 1
				if self.code[self.IP] == ']':
					level -= 1
				self.IP += 1
	
	def loopEnd(self):
		if self.tape[self.tapePointer] != 0:
			level = 1
			self.IP -= 1
			while level > 0:
				if self.code[self.IP] == '[':
					level -= 1
				if self.code[self.IP] == ']':
					level += 1
				self.IP -= 1
			self.IP += 1
	
	def __init__(self):
		self.reset()
		self.commands = {
			'>': self.moveRight,
			'<': self.moveLeft,
			'+': self.increment,
			'-': self.decrement,
			'.': self.output,
			',': self.input,
			'[': self.loopBegin,
			']': self.loopEnd
		}
		
	def setCode(self, program):
		self.code = program
		self.IP = 0
	
	def execute(self, program = None):
		self.reset()
		if program is not None:
			self.setCode(program)
		while self.IP < len(self.code):
			instruction = self.code[self.IP]
			if instruction not in self.commands:
				self.IP += 1
				continue
			self.commands[instruction]()
			self.IP += 1

