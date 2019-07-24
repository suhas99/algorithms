from itertools import combinations


def check(num, n, k):
	c = combinations(num,4)
	count = 0
	for i in c:
		if sum(i) == k:
			print(i)
			count += 1
	print(count)


T = int(input("Test cases"))
for _ in (0, T):
	N = int(input("enter n"))
	K = int(input("enter k"))
	num = list(map(int, input().split()))
	check(num, N, K)

