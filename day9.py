# loop through a list and add +2
list = [1,2,3,4,5]
length = len(list)
i = 0
while i < length:
    print(list[i])
    i += 2

#to get the desired output
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j, end="")
    print()

# fibonacci sequence
n = int(input("Enter the value: "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ",end=" ")
while(count <= n):
    print(sum,end=" ")
    count += 1
    a = b
    b = sum
    sum = a + b

#Armstrong number : A number is said to be armstrong number if it is equal to the sum of the cubes of its own digits.
# example: 153 = 1*1*1 + 5*5*5 + 3*3*3
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp%10
    sum += digit **3
    temp//=10

if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

# multiplication table of 9
num = 9
for i in range(1,11):
    print(num,'x',i,'=',num*i)

# check the program is negative or positive
num = float(input("Enter a number: "))
if num > 0:
    print("{0} is a positive number".format(num))
elif num == 0:
    print("{0} is zero".format(num))
else:
    print("{0} is negative number".format(num))


# to convert days to ages
print("Enter the days: ")
d, y, w = int(input()) , None, None
y = (int)(d/365)
w = (int)((d%365)/7)
d = (int)(d - ((y * 365)+(w)))
print(y, "Year" , w, "Weeks" , d,"Days")

# trigonometry program
import math
a = math.pi/6
print(math.sin(a))
print(math.cos(a))
print(math.tan(a))
print(math.asin(a))
print(math.acos(a))
print(math.atan(a))

# create a basic calculator
print("Choose\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")
n = int(input("Enter your choice: "))
if n == 1:
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    c=a+b
    print("Sum= ",c)
elif n == 2:
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    c = a-b
    print("Difference= ",c)
elif n == 3:
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    c = a*b
    print("Product= ",c)
elif n == 4:
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    c = a/b
    print("Quotient= ",c)
else:
    print("Invalid Choice")

