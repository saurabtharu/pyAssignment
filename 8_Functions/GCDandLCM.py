def GCD(a, b):
	"takes two integer arguments and return the Greatest Common Divisor of two numbers"
	small = a if (a < b) else b
	for i in range(1, small + 1):
		if (a % i) == 0 and (b % i) == 0:
			gcd = i
	return gcd


def LCM(a, b):
	"takes two integer arguments and return the Least Common Multiple of two numbers"
	small = a if (a < b) else b
	for i in range(1, small + 1):
		if (a % i) == 0 and (b % i) == 0:
			gcd = i
	lcm = a * b / gcd
	return lcm
