numbers = ['3', '34', '64']

"""for i in range(len(numbers)):
	numbers[i] = int(numbers[i])"""

numbers = list(map(int,numbers))
numbers[2] = numbers[2]+1
print(numbers[2])

num = [2,3,4,5,6,7]
square = list(map(lambda x: x*x, num))  
print(square)


def square(a):
	return a*a

def cube(a):
	return a*a*a

func = [square,cube]
for i in range(5):
	val = list(map(lambda x:x(i), func))
	print(val)
