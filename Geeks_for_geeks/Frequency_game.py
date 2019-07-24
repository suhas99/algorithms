def check(num, size):
	num.sort(reverse=True)
	max_value = max(num)
	Times_repeated = num.count(max_value)
	print(max_value, Times_repeated)


T = int(input("test cases"))
for _ in range(0, T):
	arr_size = int(input("array size"))
	numbers = list(map(int, input("enter array").split()))
	if len(numbers) != arr_size:
		print("array size is invalid")
	else:
		check(numbers, arr_size)
