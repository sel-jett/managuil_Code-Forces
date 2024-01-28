t = int(input())
code = "codeforces"
for _ in range(t):
	s = input()
	ans = 0
	for i in range(len(code)):
		if s[i] != code[i]:
			ans += 1
	print(ans)