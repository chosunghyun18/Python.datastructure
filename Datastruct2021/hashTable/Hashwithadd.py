class HashOpenAddr:
	def __init__(self, size=10):
			self.size = size
			self.keys = [None]*self.size
			self.values = [None]*self.size
	def __str__(self):
			s = ""
			for k in self:
					if k == None:
							t = "{0:5s}|".format("")
					else:
							t = "{0:-5d}|".format(k)
					s = s + t
			return s
	def __iter__(self):
			for i in range(self.size):
					yield self.keys[i]


	def __getitem__(self, key):
			return self.keys[key]


	def __setitem__(self, key, value):
			self.set(key, value)

	def find_slot(self, key):
			i = self.hash_function(key)
			start = i
			#H[i] 가 다른 값이 있거나
			while (self.keys[i] != None ) and (self.keys[i]!= key):
					i = (i + 1) % 10
					if (i == start):    # 한바퀴 다돌면
							return None
			return i

	def set(self, key, value=None):
			i = self.find_slot(key)
			if (i == None) : return None
			if self.keys[i] != None:  # 이미 key 값을 갖는 item이 H에 존재함 (수정)
				self.keys[i] = key  # value 값 update 후 리턴
			else :
					self.keys[i] = key
					self.values[i] = value
			return key  #value 는 none 값으로 이루어


	def hash_function(self, key):
			return key % self.size

	#key is extinct  > erase it and return
	def remove(self, key):
			i = self.find_slot(key)
			if self.keys[i]  ==  None :
					return None
			j = i
			while True:
					self.keys[i]  = None
					while True:
							j = (j + 1) % 10
							if self.keys[j] == None: return key
							#
							k =self.find_slot(self.keys[j])
							if not (i < k <= j or j < i < k or k <= j < i):  # H[j] --> H[i]
									break
					self.keys[i] = self.keys[j]
					i = j


	def search(self, key):
			i = self.find_slot(key)
			if i == None :return None
			if self.keys[i] == key:return key
			else : return None

H = HashOpenAddr()
while True:
	cmd = input().split()
	if cmd[0] == 'set':
			key = H.set(int(cmd[1]))
			if key == None: print("* H is full!")
			else: print("+ {0} is set into H".format(cmd[1]))
	elif cmd[0] == 'search':
			key = H.search(int(cmd[1]))
			if key == None: print("* {0} is not found!".format(cmd[1]))
			else: print(" * {0} is found!".format(cmd[1]))
	elif cmd[0] == 'remove':
			key = H.remove(int(cmd[1]))
			if key == None:
					print("- {0} is not found, so nothing happens".format(cmd[1]))
			else:
					print("- {0} is removed".format(cmd[1]))
	elif cmd[0] == 'print':
			print(H)
	elif cmd[0] == 'exit':
			break
	else:
			print("* not allowed command. enter a proper command!")