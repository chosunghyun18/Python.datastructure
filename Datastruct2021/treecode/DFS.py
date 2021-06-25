import sys
sys.setrecursionlimit(5000)

def DFS(G, v):
	global curr_time
	# 그래프 G의 노드 v를 DFS 방문한다
	visited[v] = True
	pre[v] = curr_time
	curr_time += 1
	for w in G[v]:
		if visited[w] == False:
			DFS(G, w)
	post[v] = curr_time
	curr_time += 1
	
def DFSAll(G):
	# 그래프 G를 DFS 방문한다
		for v in range(n):
			if visited[v] == False:
				DFS(G, v)

	

# 입력 처리
n, m = [int(x) for x in input().split()]
G = [[] for _ in range(n)]
# G 입력 받아 처리
for _ in range(m):
	a, b = [int(x) for x in input().split()]
	G[a].append(b)
	G[b].append(a)
	
for v in range(n):
	G[v].sort()
# visited, pre, post 리스트 정의와 초기화
visited = [False for x in range(n)]
pre, post = [0] * n, [0] * n
# curr_time = 1로 초기화
curr_time = 1

DFSAll(G)




# 출력
pair = list(zip([i for i in range(n)], pre))
pair.sort(key=lambda x: x[1])
for v, _ in pair:
	print(v, end=' ')
print()
for x, y in zip(pre, post):
	print(f"[{x}, {y}]", end=' ')
print() 