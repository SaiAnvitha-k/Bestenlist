#merging two python dictionaries
def Merge(Dict1,Dict2):
    return (Dict2.update(Dict1))
Dict1 = {"A:a" , "B:b" , "C:c" , "D:d" , "E:e" , "F:f"}
Dict2 = {"Ten:10" , "One:1" , "Two:2" , "Four:4" , "Six:6"}
print(Merge(Dict1,Dict2))
print(Dict2)

#remove a key from the dictionary
chocolate = {"Dairymilk":200,"fivestar":10,"Kitkat":40,"Temptations":80}
print(chocolate.pop("fivestar"))

#map two lists into a dictionary
keys = ['apple' , 'mango' , 'orange' , 'grapes']
values = ['red' , 'yellow' , 'orange' , 'blue']
fruits = dict(zip(keys , values))
print(fruits)

#find the length of the set
bts = {"rm" , "jin" , "suga " , "jhope" , "jimin" , "v" , "jk"}
print(len(bts))

#remove the intersection of 2nd set from 1st set
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set1.difference_update(set2)
print(set1)
print(set2)
