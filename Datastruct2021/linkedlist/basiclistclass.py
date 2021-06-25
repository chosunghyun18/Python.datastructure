class myList():
	def __init__(self):
		self.capacity = 2	  # myList의 용량 (저장할 수 있는 원소 개수)
		self.n = 0          # 실제 저장된 값의 개수
		self.A = [None] * self.capacity # 실제 저장 자료구조 (python의 리스트 사용) 

	def __len__(self):
		return self.n
	
	def __str__(self):
		return f'  ({self.n}/{self.capacity}): ' + '[' + ', '.join([str(self.A[i]) for i in range(self.n)]) + ']'

	def __getitem__(self, k): # k번째 칸에 저장된 값 리턴
		if self.n==0  or  -(self.n)  > k or k >  self.n - 1:
			raise IndexError
		if k < 0:
			k = self.n + k
			
		return self.A[k]

	def __setitem__(self, k, x): # k번째 칸에 값 x 저장
		if self.n == 0  or -(self.n) > k or k >  self.n - 1:
			raise IndexError
		if k < 0:
			k = self.n + k
		
		self.A[k] = x

	def change_size(self, new_capacity):
		print(f'  * changing capacity: {self.capacity} --> {new_capacity}') # 이 첫 문장은 수정하지 말 것
		B = [None]*new_capacity
		# 2. self.A의 값을 B로 옮김
		for i in range(self.n):
			B[i] = self.A[i]
			# 3. del self.A  (A 지움)
		del self.A
		self.A = B

		# 5. self.capacity = new_capacity
		self.capacity = new_capacity
	
	def append(self, x):
		if self.n == self.capacity: # 더 이상 빈 칸이 없으니 capacity 2배로 doubling
			self.change_size(self.capacity*2)
			self.A[self.n] = x     # 맨 뒤에 삽입
			self.n += 1            # n 값 1 증가
		else :
			self.A[self.n] = x
			self.n += 1

	def pop(self, k=None): # A[k]를 제거 후 리턴. k 값이 없다면 가장 오른쪽 값 제거 후 리턴
		if self.n == 0 or -(self.n) > k or k > self.n - 1:
			raise IndexError
		if k < 0:
			k = self.n + k
		
		if self.capacity >= 4 and self.n <= self.capacity // 4:  # 실제 key 값이 전체의 25% 이하면 halving
				self.change_size(self.capacity // 2)
		
		if k == None :
			k = self.n -1
			x = self.A[k]
			
		else :
			x = self.A[k]
		
		for i in range(k+1, self.n):
			self.A[i - 1] = self.A[i]
		
		self.A[self.n-1] = None
		self.n -= 1
		
		return x

	def insert(self, k, x):
		if self.n==0:
			raise IndexError
			
		if -(self.n) > k or k >  self.n - 1 :
			raise IndexError
		
		if k < 0:
			k = self.n + k
			
		if self.n == self.capacity: # 더 이상 빈 칸이 없으니 capacity 2배로 doubling
			self.change_size(self.capacity*2)
		
		for i in range(self.n-k):
			self.A[-(self.capacity-self.n+i)] = self.A[-(self.capacity-self.n+i+1)]
		
		self.A[k] = x 
		
		self.n += 1

	def size(self) :
		return self.capacity
	
	
	
L = myList()
while True:
    cmd = input().strip().split()
    if cmd[0] == 'append':
        L.append(int(cmd[1]))
        print(f"  + {cmd[1]} is appended.")
    elif cmd[0] == 'pop':
        if len(cmd) == 1:
            idx = -1
        else:
            idx = int(cmd[1])
        try:
            x = L.pop(idx)
            print(f"  - {x} at {idx} is popped.")
        except IndexError:
            if len(L) == 0:
                print("  ! list is empty.")
            else:
                print(f"  ! {idx} is an invalid index.")
    elif cmd[0] == 'insert':
        try:
            L.insert(int(cmd[1]), int(cmd[2]))
            print(f"  + {cmd[2]} is inserted at index {cmd[1]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'get': # getitem A[k]
        try:
            L[int(cmd[1])]
            print(f"  @ L[{cmd[1]}] --> {L[int(cmd[1])]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'set': # setitem A[k] = x
        try:
            L[(int(cmd[1]))] = int(cmd[2])
            print(f"  ^ L[{cmd[1]}] <-- {cmd[2]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'size':
        print("  ? capacity =", L.size())
    elif cmd[0] == 'print':
        print(L)
    elif cmd[0] == 'exit':
        print('bye~')
        break
    else:
        print(" ? invalid command! Try again.")