print("length of tuple")
t=[44	,33,55]
print(t)
print(t[2])
print(len(t))


print("largest and smallest in tuple")
print(max(t))
print(min(t))


print("product of all elements")
t=(1,3,5,7,9,11)
q=1
for a in range(0,6):
	k=t[a]
	q=k*q
print(q)


print("create sets ")
s=set([1,2,3,4,5])
print(s)
print(s.update([6,7,8]))
print(s)


print("create dictionary")
l=[]
d={}
for x in range(0,4):
	name=input("enter name:")
	marks=int(input("enter marks:"))
	d[name]=marks
	l.append(marks)
print(d)
l.sort()
print(l)


print("count a no occurrence of each letter")
x="MISSISSIPPI"
a=x.count('M')
b=x.count('I')
c=x.count('S')
d=x.count('P')
f={'M':a,'I':b,'S':c,'p':d}
print("the no. of occurance of each letter of MISSISSIPPI")
print(f)	
