#Q-1.CREATE A LIST.
a=['TEJU','TANMAY','SAM','TANUJ']
print(a)

#Q-2.CONCATINATE LIST.
a=['MANGO','APPLE','BANANA','LITCHI']
b=('mango' + 'litchi')
print(b)

#Q-3.COUNT THE OCCURANCE IN LIST.
d=[8,9,1,3,4,5,3,4,3,3]
print(d.count(3))

#Q-4.SORT THE LIST.
s=['SUBU','NIHIT','ARPIT','SIMRAN','GOLI']
s.sort()
print(s)

#Q-5.CONCATINATE AND SORT 2 SORTED ARRAYS.
a=[2,5,7,9,0]
b=[1,4,11,8]
c=a+b
c.sort()
print(c)

#Q-6.COUNT EVEN AND ODD NUMBER IN LIST.
list=[1,2,3,6,8,7]
a=0
b=0
for i in list:
     if not i%2:
        a+=1
     else:
        b+=1
print("even no.",a)
print("odd no.",b)
        
#Q-7.PRINT A TUPLE IN REVERSE ORDER.
z=(1,2,3,4)
k=slice(-1,-5,-1)
print(z[k])


#Q-8.FIND LARGEST AND SMALLEST ELEMENTS OF A TUPLE.
s=[4,5,6,7,8,9]
print("max element is ",max(s))
print("min element is ",min(s))

#Q-9.CONVERT A STRING INTO UPPERCASE.
f="subina"
print(f.upper())

#Q-10.CHECK IF STRING CONTAINS ALL NUMERIC CHARACTERS.
n="34567"
print (n.isnumeric())
        
#Q-11.REPLACE THE GIVEN STRING WITH YOUR NAME.
a="hey there!"
print(a.replace("there","subina"))
