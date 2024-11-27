'''
Author: Nicholas Theisen
KUID: 3124859
Date: 09/12/2024
Lab: lab1
Last modified: 09/25/2024
Purpose: Program containing node based implementation of a linked queue
'''
from node import Node

class LinkedQueue:
	def __init__(self):
		self._front = None
		self._back = None

	def is_empty(self):
		return self._front is None 

	def enqueue(self, entry):
		temp = Node(entry)
		if self.is_empty():
			self._front = temp
			self._back = temp
		else:
			self._back.next = temp
			self._back = temp

	def dequeue(self):
		temp = self._front
		if self.is_empty():
			raise RuntimeError("Queue is Empty.")
		
		self._front = self._front.next
		if self._front is None:
			self._back = None
		return temp.entry

	def peek_front(self):
		if self.is_empty():
			raise RuntimeError("Queue is Empty.")
		else:
			return self._front.entry

