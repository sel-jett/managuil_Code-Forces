t = int(input())
for _ in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	ans = 0
	cur = 0
	for i in range(n):
		if a[i] == 0:
			cur += 1
		else:
			ans = max(ans, cur)
			cur = 0
	ans = max(ans, cur)
	print(ans)