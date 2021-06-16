#create a list of n integers
A=[100,500,300,800,200,700,400,900]
#add an item
A.append(1000)
print(A)
#delete an item
del A[1]
print(A)
#max value
B = max(A)
print(B)
#min value
C = min(A)
print(C)

#create a tuple and print the reverse of the tuple
x = ('a' ,'l','m','v','n','c','r')
y = reversed(x)
print(tuple(y))

#create a tuple and convert it into list
my_tuple = ('mango','orange' , 'berry',1200,'ab')
my_list = list(my_tuple)
print(my_list)
