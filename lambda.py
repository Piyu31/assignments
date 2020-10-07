#minus = lambda x,y:x-y
#print(minus(9,4))


#def a_first(a):
#	return a[1]

a=[[23,12],[43,87],[33,59]]
#a.sort(key=a_first)
a.sort(key=lambda x:x[1])
print(a)	