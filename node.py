'''
Author: Nicholas Theisen
KUID: 3124859
Date: 09/12/2024
Lab: lab1
Last modified: 09/19/2024
Purpose: Program containing node class to be used for stack and queue
'''
class Node:
	def __init__(self, entry):
		self.entry = entry
		self.next = None