i = 1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1

print("end of loop")

i = 0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

nums=[1,2,3,4,5]
for val in nums:
    print(val)

# print the element of the following list using a loop
listt=[1,4,9,16,25,36,49,64,81,100]
for prnt in listt:
    print(prnt)

for i in range(3,10,2):#(start.optional,stop,step size.optional)
    print(i)
n=int(input("Enter a number")) 
for i in range(1,11):
    print(n*i)     