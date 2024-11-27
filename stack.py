'''
Author: Nicholas Theisen
KUID: 3124859
Date: 09/12/2024
Lab: lab1
Last modified: 09/25/2024
Purpose: Program containing node based implementation of a stack
'''
from node import Node

class Stack:
	def __init__(self):
		self._top = None

	def push(self, entry):
		temp = Node(entry)
		temp.next = self._top
		self._top = temp

	def pop(self):
		temp = self._top
		if self.is_empty():
			raise RuntimeError("Stack Is Empty.")
		else:
			self._top = self._top.next
		return temp.entry

	def peek(self):
		if self.is_empty():
			raise RuntimeError("Stack Is Empty.")
		return self._top.entry

	def is_empty(self):
		return self._top is None


