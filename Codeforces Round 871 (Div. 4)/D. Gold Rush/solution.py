t = int(input())

def ft_get_a_b(n):
	return (n // 3, n - (n // 3))

#def rev(n, m):
#	if (n == m):
#		return (1)
#	elif (n < m):
#		return (0)
#	elif (n % 3 != 0):
#		return (0)
#	elif (n % 3 == 0):
#		a, b = ft_get_a_b(n)
#		return rev(a, m) + rev(b, m)


for _ in range(t):
	n, m = map(int, input().split())
	if n == 1 and m == 1:
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

