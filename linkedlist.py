'''
Author: Nicholas Theisen
KUID: 3124859
Date: 09/12/2024
Lab: lab1
Last modified: 10/03/2024
Purpose: Program containing linkedlist
'''
from node import Node

class LinkedList:
	def __init__(self):
		self._front = None
		self._length = 0

	def length(self):
		return self._length

	def get_entry(self, index):
		if (index >= self._length) or (index < 0):
			raise IndexError
	
		else:
			jumper = self._front
			for i in range(index):
				jumper = jumper.next
			
			return jumper.entry

	def insert(self, index, entry):
		if (index < 0) or (index > self._length):
			raise IndexError

		
		elif index == 0:
			temp = Node(entry)
			temp.next = self._front
			self._front = temp

		else:
			temp = Node(entry)
			jumper = self._front
			for i in range(index - 1):
				
				if jumper.next is None:
					raise IndexError
				jumper = jumper.next

			temp.next = jumper.next
			jumper.next = temp
		
		self._length += 1

	def remove(self, index):
		if (index < 0) or (index > self._length - 1):
			raise IndexError

		elif index == 0:
			self._front = self._front.next

		else:
			jumper = self._front
			for i in range(index - 1):
				jumper = jumper.next

			jumper.next = jumper.next.next
		self._length -= 1

	def set_entry(self, index, entry):
		if (index < 0) or (index > self._length - 1):
			raise RuntimeError
		else:
			jumper = self._front
			for i in range(index):
				jumper = jumper.next
			jumper.entry = entry

	def clear(self):
		self._front = None
		self._length = 0
