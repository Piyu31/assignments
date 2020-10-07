from functools import reduce
list1 = [1,2,3,4,12]
"""num = 0
for i in list1:
	num = num+i"""
num = reduce(lambda x,y:x+y, list1)
nos =reduce(lambda a,b:a*b, list1)
print(num)
print(nos)