def check():
	b = num[::-1]

	if num == b:
		print("Yes")
	else:
		print("no")


T = int(input("no of test cases"))
for _ in (0, T):
	num = list(map(str, input().upper()))
	check(num)
