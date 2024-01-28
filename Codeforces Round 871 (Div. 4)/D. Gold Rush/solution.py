t = int(input())

def ft_get_a_b(n):
	return (n // 3, n - (n // 3))

for _ in range(t):
	n, m = map(int, input().split())
	if n == 1:
		print("YES")
	elif (n % 3 != 0) or m > n:
		print("NO")
	else:
		prev = set()
		prev.add(n)
		i = 1
		founded = False
		while (i and not founded):
			i = 0
			new = set()
			for k in prev:
				if k % 3 == 0:
					a, b = ft_get_a_b(k)
					new.add(a)
					new.add(b)
					i = 1
			if m in new:
				founded = True
			prev = new
		
		if (founded):
			print("YES")
		else:
			print("NO")

