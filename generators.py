def gen(n):
	for i in range(n):
		#return i
		yield i
g =gen(4)
#g.__next__()
print(g.__next__())
print(g.__next__())
print(g.__next__())
#for i in g:
	#print(i)