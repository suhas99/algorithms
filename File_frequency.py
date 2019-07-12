def check(numbers, target):
	# checks the number of times the no is repeated
	s = 0
	s += numbers.count(target)
	print(s)


def check1(numbers, target, size):
	l = []
	count = 0
	for i in range(0, len(numbers)):
		l = numbers[i:size]
		size += 1
		b = set(l)
	if len(b) == 1:
		s = b.pop()
		if s == target:
			count += 1
	print("the pattren frequencey is ", count)


N = int(input("Enter input test cases"))
for _ in range(0, N):
	size = int(input("enter the size"))
	numbers = list(map(int, input().split()))
	target = int(input())
	check(numbers, target)
	check1(numbers, target, size)
