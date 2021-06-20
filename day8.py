#merging two dictionaries
d1 = {'a' : 10, 'b' : 20, 'c' : 30}
d2 = {'d' : 40, 'e' : 50, 'f' : 60}
d = d1.copy()
d.update(d2)
print(d)

#sorting list and convert into set
a = [100,30,500,60,20,90,120]
a.sort(reverse=True)
print(a)
x = set(a)
print(x)

# list the items in dictionary and sorting with & without function
dict1 = {'a':10,'b':5,'c':25,'d':15,'e':20}
l = len(dict1)
print(l)
# with function
sort = sorted(dict1.values())
print(sort)
#without function
list1 = []
values = dict1.values()
my_list = list(values)

while my_list:
    min = my_list[0]
    for x in my_list:
        if x < min:
            min = x
    list1.append(min)
    my_list.remove(min)

print(list1)

#to get a string from user input and change the occurrence
Q = input("Enter your age: ")
string_a = "Jack is" +" " + Q + " " +"years old"
string_b = string_a.replace("Jack","Joey")
print(string_a)
print(string_b)

#change the first char to capital letters
W = input("Enter your age: ")
string_c = "Jack is" +" " + W + " " +"years old"
string_d = string_c.title()
print(string_d)

#find the repeated items in list
list_a = [10,1,3,2,3,1,7,6,9,4,6]
set_a = set(list_a)
if len(list_a) != len(set_a):
    print("Contains Duplicate Values")
else:
    print("Does not contain Duplicate Values")

# sum of three elements and division by input value
x = int(input("Enter a number: "))
num = [2,8,4]
y = sum(num)
print(y)
result = y/x
print(result)



#mean median and mode
import  statistics
a_list = [3,4,2]
Mean = statistics.mean(a_list)
Median = statistics.median(a_list)
Mode = statistics.mode(a_list)
print(Mean)
print(Median)
print(Mode)

#swapcase
string_a = "hELLO wORLD"
print(string_a.swapcase())
string_b = "mango"
print(string_b.swapcase())

#integer into binary and octa decimal
int1 = int(input("Enter a number: "))
print(bin(int1),"is binary")
print(oct(int1),"is octal")
