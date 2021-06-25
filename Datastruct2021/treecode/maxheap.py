#make it max heap
class AdaptedHeap:
    def __init__(self):
        self.A = []
        self.D = {}
    def __str__(self):
        return str(self.A)
    def __len__(self):
        return len(self.A)

    def insert(self,key):
        self.A.append(key)
        self.D[key] = len(self.A) -1
        self.heapify_up(len(self.A)-1)
        return self.D[key]

    def heapify_up(self, k):  # 올라가면서 A[k]를 재베치 여기서 리스트의 k 인덱스
        while k > 0 and self.A[(k - 1) // 2] < self.A[k]:
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]
            self.D[self.A[k]], self.D[self.A[(k - 1) // 2]] = self.D[self.A[(k - 1) // 2]], self.D[self.A[k]]
            k = (k - 1) // 2

    def heapify_down(self, k, n):
        # code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
        # n = 힙의 전체 노드수 [heap_sort를 위해 필요함]
        # A[k]가 힙 성질을 위배한다면, 밑으로
        # 내려가면서 힙성질을 만족하는 위치를 찾는다
        while 2 * k + 1 < n:  # leaf node 전까지
            L, R = 2 * k + 1, 2 * k + 2
            if L < n and self.A[L] > self.A[k]:
                m = L
            else:
                m = k

            if R < n and self.A[R] > self.A[m]:
                m = R  # m = A[k], A[L], A[R] 중 최소값의 인덱스

            if m != k:  # A[k]가 최대값이 아니라면 힙 성질 위배
                self.A[k], self.A[m] = self.A[m], self.A[k]
                self.D[self.A[k]], self.D[self.A[m]] = self.D[self.A[m]], self.D[self.A[k]]
                k = m
            else:
                break

    def find_max(self):
        # 빈 heap이면 None 리턴, 아니면 min 값 리턴
        if len(self.A) == 0: return None
        key = self.A[0]
        return key

    def delete_max(self):
        # 빈 heap이면 None 리턴, 아니면 min 값 지운 후 리턴
        if len(self.A) == 0: return None
        key = self.A[0]
        self.D[key], self.D[self.A[len(self.A) - 1]] = self.D[self.A[len(self.A) - 1]], self.D[key]
        self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0]
        self.A.pop()  # 실제로 리스트에서 delete!
        del self.D[key]
        self.heapify_down(0, len(self.A))
        return key

    def update_key(self, old_key, new_key):
        # old_key가 힙에 없으면 None 리턴
        if len(self.A) == 0: return None
        if not old_key in self.D: return None
        k = self.D[old_key]
        self.D[new_key] = self.D.pop(old_key)  # 70 71 could be chage line
        self.A[k] = new_key
        if new_key > old_key:
            self.heapify_up(k)
        else:
            self.heapify_down(k, len(self.A))

        return self.D[new_key]


# 아래 명령 처리 부분은 수정하지 말 것!
H = AdaptedHeap()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        key = int(cmd[1])
        loc = H.insert(key)
        print(f"+ {int(cmd[1])} is inserted")
    elif cmd[0] == 'find_max':
        m_key = H.find_min()
        if m_key != None:
            print(f"* {m_key} is the minimum")
        else:
            print(f"* heap is empty")
    elif cmd[0] == 'delete_max':
        m_key = H.delete_min()
        if m_key != None:
            print(f"* {m_key} is the minimum, then deleted")
        else:
            print(f"* heap is empty")
    elif cmd[0] == 'update':
        old_key, new_key = int(cmd[1]), int(cmd[2])
        idx = H.update_key(old_key, new_key)
        if idx == None:
            print(f"* {old_key} is not in heap")
        else:
            print(f"~ {old_key} is updated to {new_key}")
    elif cmd[0] == 'print':
        print(H)
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")