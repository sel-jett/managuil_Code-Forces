t = int(input())
res = []
for _ in range(t):
	hashmap = {}
	n = int(input())
	for i in range(n):
		m, s = input().split()
		m = int(m)
		c = int(s, 2)
		if not c in hashmap:
			hashmap[c] = []
		hashmap[c].append(m)
	
	for key in hashmap:
		hashmap[key].sort()
	
	time = -1
	if 1 in hashmap and 2 in hashmap:
		time = hashmap[1][0] + hashmap[2][0]
	if 3 in hashmap:
		if time == -1:
			time = hashmap[3][0]
		else:
			time = min(time, hashmap[3][0])
	print(time)
	print(hashmap)
	res.append(time)

print(res)