# 1. class Node 선언 부분
class Node:
		def __init__(self, key=None):
				self.key = key
				self.prev = self
				self.next = self
		def __str__(self):
				return str(self.key)

# 2. class DoublyLinkedList 선언부분
class DoublyLinkedList:
		def __init__(self):
				self.head = Node() # create an empty list with only dummy node

		def __iter__(self):
				v = self.head.next
				while v != self.head:
						yield v
						v = v.next
		def __str__(self):
				return " -> ".join(str(v.key) for v in self)
		def printList(self):
				v = self.head.next
				print("h -> ", end="")
				while v != self.head:
						print(str(v.key)+" -> ", end="")
						v = v.next
				print("h")
