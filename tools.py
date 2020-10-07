from itertools import *
import operator
#zip
list1 = [1,2,3]
list2 = ['a', 'b', 'c']  
lee = zip(list1,list2)  
print("The zip gives us:",list(lee))  

#product
lee = product(list1,list2)
print("The products gives us:",list(lee))

#iter
a = iter('Hello')
print(a)
print("The iter list is:",list(a))

#permutations
lot = [5,6,7]
perm = permutations(lot)
print("The permuts are:",list(perm))

#combinations
com = [8,9,10]
comb = combinations(com,2)
print("The combos are:",list(comb))

#combination_with_replacement
com_wr=combinations_with_replacement(com,2)
print("The combinations_with_replacement are:",list(com_wr))  

#accumulate
ac = [7,9,15,11,12]
acum = accumulate(ac)
acus = accumulate(ac, func=operator.mul)
accus = accumulate(ac, func=max)
print(ac)
print("The accumulate sum gives:",list(acum))
print("The accumulate mul gives:",list(acus))
print("The accumulate max gives:",list(accus))

#groupby
def smaller_than_3(x):
	return x<3
gr =[1,2,6,7]
group_obj = groupby(gr, key=smaller_than_3)
print("The groupby serves:")
for key, value in group_obj:
	print(key,value)
	print(key,list(value))

#count
for i in count(10):
	print(i)
	if i == 15:
		break
"""
#cycle
a=[1,2,3]
for i in cycle(a):
	print(i)
"""
#repeat
a=[1,2,3]
for i in repeat(2,4):
	print(i)

