import time

localtime = time.asctime(time.localtime(time.time()))
print(localtime)


initial = time.time()
k=0
while(k<5):
	print("This is harry")
	time.sleep(1)
	k+=1
print("While loop ran in" , time.time()-initial,"seconds")


initial_2 = time.time()
for i in range(5):
	print("This is ron")
print("For loop ran in" , time.time()-initial_2,"seconds")
