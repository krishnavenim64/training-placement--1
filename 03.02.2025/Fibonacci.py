nterms=int(input("no of terms"))
n1,n2=0,1
count=0
if nterms<=0:
print("enter positive nums:")
elif nterms==1:
print("1")
else:
print("fibonacci series")
while count<nterms:
   print(n1)
   nth=n1+n2
   n1=n2
   n2=nth
   count+=1
Which program 
