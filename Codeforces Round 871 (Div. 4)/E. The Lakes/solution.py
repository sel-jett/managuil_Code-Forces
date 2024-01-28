from collections import deque 

def bfs(matrix, sr, sc):
	rows = len(matrix)
	cols = len(matrix[0])
	
	directions = {
		(0, 1),
		(1, 0),
		(-1, 0),
		(0, -1)
	}
	queue = deque()
	queue.append((sr, sc))
	visited.add((sr, sc))
	cur = matrix[sr][sc]
	while (queue):
		r, c = queue.popleft()
		for dr, dc in directions:
			nr = r + dr
			nc = c + dc
			if 0 <= nr < rows  and 0 <= nc < cols and matrix[nr][nc] != 0 and (nr, nc) not in visited:
				cur += matrix[nr][nc]
				visited.add((nr, nc))
				queue.append((nr, nc))
	return cur
	
t = int(input())
for _ in range(t):
	visited = set()
	Max = 0
	n, m = map(int, input().split())
	matrix = []
	for r in range(n):
		matrix.append(list(map(int, input().split())))
	
	for r in range(n):
		for c in range(m):
			if matrix[r][c] != 0 and (r, c) not in visited:
				Max = max(Max, bfs(matrix, r, c))
	print(Max)
