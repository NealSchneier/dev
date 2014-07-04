#!/usr/bin/env python

class queue(object):
	def __init__(self):
		self.head = 0
		self.tail = 0
		self.list = []
		self.n = 0

	def enqueue(self, element):
		self.list.append(element)
		self.tail += 1
		self.n += 1

	def dequeue(self):
		if self.n == 0:
			return None
		e = self.list[self.head]
		self.head += 1
		self.n -= 1
		return e

	def size(self):
		return self.n

	def elements(self):
		return [self.list[i] for i in xrange(self.head, self.tail)]

class stack(object):
	def __init__(self):

		self.n = 0
		self.list = []

	def push(self, element):
		self.list.append(element)
		self.n += 1

	def pop (self):
		#return element
		if self.n == 0: 
			return None

		e = self.list[self.n-1]
		self.n -= 1
		return e

	def size(self):
		return self.n
	def elements(self):
		return [self.list[i] for i in xrange(0, self.n)]

class Node:
	def __init__(self):
		self.value = None
		self.next = None
	
class linkedList(object):
	def __init__(self):
		self.current = None

	#puts in front and returns
	def addNode(self, value):
		temp = Node()
		temp.data = value
		temp.next = self.current
		return temp
	
	def hasNext(self):
		if self.current == None:
			return False
		return True




def reverseString(word):
	list = []
	for i in range( len(word), 0, -1):
		list.append(word[i-1])
	
	print list	

def myQueue():

	temp = queue()
	temp.enqueue("1")
	temp.enqueue("2")

	print temp.size()

def myStack():
	temp = stack()
	temp.push("5")
	temp.push("4")
	temp.pop()
	temp.pop()
	print temp.elements()


