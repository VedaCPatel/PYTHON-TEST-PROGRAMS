#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number
num=int(input("Enter a number:"))
l=[]
for i in range(1,num+1):
    if num%i==0:
        a=l.append(i)
print(l,"is the list of divisors of",num)








