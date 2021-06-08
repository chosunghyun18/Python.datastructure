
"""
start in node key 0

input (given)

>node number n
>edge number
>u v w(edge:move u to v with weight w)

input example)

10    #n
14   # edge
0 1 5
9 3 3
0 2 8
1 2 8
3 4 8
2 4 5
0 3 1
6 3 7
3 9 6
4 0 4
3 2 8
0 4 3
8 0 1
4 2 1

"""











# get number of  node
n = int(input())

# get num of edge
edge = int(input())

# make graph = g
g = []
for i in range(n):
    g.append("inf")

for x in range(edge):
    cmd = input().split()
    if g[int(cmd[0])] == "inf":
        g[int(cmd[0])] = []
    g[int(cmd[0])].append(int(cmd[1]))
    g[int(cmd[0])].append(int(cmd[2]))

for i in range(n):
    if g[i] == "inf":
        g[i] = 0

# dist[v] : dist[v]:min each u|u>v { dist[u],weight(u->v)}
dist = []  # 0-> 0 dist = 0
for i in range(n):
    dist.append(100000000000 + i)
check = []
for i in range(n):
    check.append(0)

dist[0] = 0


# Heap for distance
class AdaptedHeap:  # min_heap으로 정의함!
    def __init__(self):
        self.A = []


    def __str__(self):
        return str(self.A)

    def __len__(self):
        return len(self.A)

    # key 값이 최종 저장된 index를 리턴한다!
    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A) - 1)
        return 0

    def heapify_up(self, k):  # 올라가면서 A[k]를 재베치 여기서 리스트의 k 인덱스
        while k > 0 and self.A[(k - 1) // 2] > self.A[k]:
            self.A[k], self.A[(k - 1) // 2] = self.A[(k - 1) // 2], self.A[k]

            k = (k - 1) // 2

    def heapify_down(self, k, n):
        # code here: key 값의 index가 변경되면 그에 따라 D 변경 필요
        # n = 힙의 전체 노드수 [heap_sort를 위해 필요함]
        # A[k]가 힙 성질을 위배한다면, 밑으로
        # 내려가면서 힙성질을 만족하는 위치를 찾는다
        while 2 * k + 1 < n:  # leaf node 전까지
            L, R = 2 * k + 1, 2 * k + 2
            if L < n and self.A[L] < self.A[k]:
                m = L
            else:
                m = k

            if R < n and self.A[R] < self.A[m]:
                m = R  # m = A[k], A[L], A[R] 중 최소값의 인덱스

            if m != k:  # A[k]가 최대값이 아니라면 힙 성질 위배
                self.A[k], self.A[m] = self.A[m], self.A[k]

                k = m
            else:
                break

    def find_min(self):
        # 빈 heap이면 None 리턴, 아니면 min 값 리턴
        if len(self.A) == 0: return None
        key = self.A[0]
        return key

    def delete_min(self):
        # 빈 heap이면 None 리턴, 아니면 min 값 지운 후 리턴
        if len(self.A) == 0: return None
        key = self.A[0]
        self.A[0], self.A[len(self.A) - 1] = self.A[len(self.A) - 1], self.A[0]
        self.A.pop()  # 실제로 리스트에서 delete!
        self.heapify_down(0, len(self.A))
        return key

    def update_key(self, old_key, new_key):
        # old_key가 힙에 없으면 None 리턴
        if len(self.A) == 0: return None

        for x in range(len(self.A)):
            if old_key == self.A[x]:
                self.A[x] = new_key
                k=x
                break

        if new_key < old_key:
            self.heapify_up(k)
        else:
            self.heapify_down(k, len(self.A))

        return 0


H = AdaptedHeap()
# insert dist in heap
for x in dist:
    H.insert(x)


while H:
    # 최소 거리 노드 출력

    pd = H.delete_min()  # p is presesnt point node , distance
    for x in range(len(dist)):
        if dist[x] == pd and check[x] == 0:
            pn = x
            break
    check[pn] = 1



    # 1.가지 않은 인접 한 노드 갱신
    if g[pn] != 0 :
        for x in range(len(g[pn]) // 2):
            # 인접 노드 번호 =(nn) near node
            nn = g[pn][2 * x]
            # 거리 갱신 relax
            if check[nn] == 0:  # 방문 하지 않은 노드
                if dist[nn] > dist[pn] + g[pn][2 * x + 1]:
                    H.update_key(dist[nn], dist[pn] + g[pn][2 * x + 1])
                    dist[nn] = dist[pn] + g[pn][2 * x + 1]



for x in dist:
    if x < 100000000000:
        print(x,end=" ")
    else:
        print("inf",end=" ")
