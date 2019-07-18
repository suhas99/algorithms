from math import *

T = int(input("No of test cases"))


def check1(base, exp1, mod):
	exp1 = exp1 * log(base)
	res = exp(exp1)
	print(res)
	res = exp(exp1) % mod
	print(res)


def check(base, exp, mod):
	res=1
	while exp > 0:
		res *= base
	result = res
	print(result)
	result = result % mod
	print(result)


for _ in range(0, T):
	A, B, C = map(float, input().split())
	check(A, B, C)
    #check1(A, B, C)
