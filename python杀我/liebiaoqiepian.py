a=[x for x in "hellopython"]
number=0
for chart in a:
	number+=1
print(number)
print(a[::-1])
for i in range(1,len(a)+9,2):
	a.insert(i," ")
print(a)
