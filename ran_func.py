#used in ludo
#when we require such numbers which are not known earlier e.g captcha,otp or any type of serial numbers,then in this situation we need random numbers

#randrange()--> always returns n integer value random.randrange(20)-->0 to 19.
import random
ran = random.randrange(20)
print(ran)

dom = random.randrange(30,40)
print(dom)

#random()--> this generates floating point value between 0 and 1, including 0 but excluding 1.
pox = random.random()
print(pox)

#randint()--> this takes two parameters a,b one is lower and the other is upper limit.It returns integer.
let= random.randint(2,6)
print(let)

#uniform()--> return floating point number between two given numbers. include lower limit exclude upper limit
uni = random.uniform(4,7)
print(uni)

#choice()-->used for random selection from list,tuple or string
pl = ['C', 'C++', 'Python', 'C#', 'JAVA'] #list
her = random.choice(pl)
print(her)

t=(45,67,89,76)
tup = random.choice(t)
print(tup)

#shuffle()-->this method can shuffle the items of a given list
que = ['C', 'C++', 'Python', 'C#', 'JAVA']
random.shuffle(que)
print(que)