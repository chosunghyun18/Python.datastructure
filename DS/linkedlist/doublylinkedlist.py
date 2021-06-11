class Node:
	def __init__(self, key=None):
		self.key = key
		self.prev = self
		self.next = self
	def __str__(self):
		return str(self.key)

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
	def first(self):
		if self.isEmpty(): return None
		return self.head.next

	def last(self):
		if self.isEmpty(): return None	
		return self.head.prev

	def splice(self, a, b, x):  # cut [a..b] after x
			if a == None or b == None or x == None:
				return None
			a.prev.next = b.next
			b.next.prev = a.prev
			x.next.prev = b
			b.next = x.next
			a.prev = x
			x.next = a

	def moveAfter(self, a, x):
		self.splice(a, a, x)

	def moveBefore(self, a, x):
		self.splice(a, a, x.prev)

	def insertAfter(self, x, key):
		self.moveAfter(Node(key), x)

	def insertBefore(self, x, key):
		self.moveBefore(Node(key), x)

	def pushFront(self, key):
		self.insertAfter(self.head, key)

	def pushBack(self, key):
		if key == None:
			return None
		self.insertBefore(self.head, key)

	def search(self, key=None):
		if self.head == None or key == None:
			return None
		v = self.head
		while v.next != self.head:
			if v.key == key:
				return v  # return Node which has a given key
			else:
				v = v.next
		if key == v.key:
			return v
		return None

	def deleteNode(self, x):  # delete x  , x will given inNode
		if x == None:
			return None
		if self.head == x:
			self.head = self.head.next
			self.head = self.head.prev
		x.prev.next, x.next.prev = x.next, x.prev

	def popFront(self):
		if self.head.next == self.head:
			return None
		key = self.head.next.key
		self.deleteNode(self.head.next)
		return key

	def popBack(self):
		if self.head.next == self.head:
			return None
		key = self.head.prev.key
		self.deleteNode(self.head.prev)
		return key
	
	def findMax(self):
		if self.head.next == self.head.prev:
			if self.head.next != None:
				return self.head.next.key
			else: return None
		v=self.head
		v=v.next
		maxv = v.key
		while v.next != self.head:
			if maxv < v.next.key:
				maxv = v.next.key
			v = v.next
		return maxv	# return key variable

	
	def deleteMax(self):
		tmp = self.findMax()
		v =self.search(tmp)
		self.deleteNode(v)
		return tmp
	
	def sort(self):
		if self.head ==None:
			return None 
		
		if self.head.next.next ==self.head:
			return self
		count = 0
		while self.head :
			tmp = self.findMax()
			v = self.search(tmp)
			self.moveAfter(v,self.head)
			self.deleteNode(v)
			if count == 0 :
				prevn = Node(tmp)
			if count >0 :
				newnode = Node(tmp)
				prevn.prev = newnode
				newnode.next = prevn
			count += 1
			prevn = prevn.prev
			if self.head.next == self.head.prev:
				tmp = self.findMax()
				v = self.search(tmp)
				self.moveAfter(v, self.head)
				self.deleteNode(v)
				if count == 0:
					first = tmp
					prevn = Node(tmp)
				if count > 0:
					newnode = Node(tmp)
					prevn.prev = newnode
					newnode.next = prevn
				count += 1
				prevn = prevn.prev
				while prevn != prevn.next:
					self.insertBefore(self.head,prevn.key)
					prevn = prevn.next
				self.insertBefore(self.head,prevn.key)
				return self
	
	def isEmpty(self):
		if self.head == self.head.next:
			return True
		else:
			return False

L = DoublyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == 'pushF':
		L.pushFront(int(cmd[1]))
		print("+ {0} is pushed at Front".format(cmd[1]))
	elif cmd[0] == 'pushB':
		L.pushBack(int(cmd[1]))
		print("+ {0} is pushed at Back".format(cmd[1]))
	elif cmd[0] == 'popF':
		key = L.popFront()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Front".format(key))
	elif cmd[0] == 'popB':
		key = L.popBack()
		if key == None:
			print("* list is empty")
		else:
			print("- {0} is popped from Back".format(key))
	elif cmd[0] == 'search':
		v = L.search(int(cmd[1]))
		if v == None: print("* {0} is not found!".format(cmd[1]))
		else: print("* {0} is found!".format(cmd[1]))
	elif cmd[0] == 'insertA':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 뒤에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertAfter(x, int(cmd[2]))
			print("+ {0} is inserted After {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'insertB':
		# inserta key_x key : key의 새 노드를 key_x를 갖는 노드 앞에 삽입
		x = L.search(int(cmd[1]))
		if x == None: print("* target node of key {0} doesn't exit".format(cmd[1]))
		else:
			L.insertBefore(x, int(cmd[2]))
			print("+ {0} is inserted Before {1}".format(cmd[2], cmd[1]))
	elif cmd[0] == 'delete':
		x = L.search(int(cmd[1]))
		if x == None:
			print("- {0} is not found, so nothing happens".format(cmd[1]))
		else:
			L.deleteNode(x)
			print("- {0} is deleted".format(cmd[1]))
	elif cmd[0] == "first":
		print("* {0} is the value at the front".format(L.first()))
	elif cmd[0] == "last":
		print("* {0} is the value at the back".format(L.last()))
	elif cmd[0] == "findMax":
		m = L.findMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key is", m)
	elif cmd[0] == "deleteMax":
		m = L.deleteMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key", m, "is deleted.")
	elif cmd[0] == 'sort':
		L = L.sort()
		L.printList()
	elif cmd[0] == 'print':
		L.printList()
	elif cmd[0] == 'exit':
		break
	else:
		print("* not allowed command. enter a proper command!")