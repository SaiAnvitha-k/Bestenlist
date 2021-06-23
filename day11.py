#create a module with list
#creating module.py file
a = ["cherry","apple","orange","mango","avocado"]
#importing the module in another file and changing a value in list
#creating another file 
from module import a
a[2] = "berry"
print(a)


#installing pandas 
import pandas as pd
x = pd.DataFrame({'A':[1,2,3,4], 'B':[5,6,7,8], 'C':[10,11,12,13]});
print(x)

#import a module that picks random number
# importing random module
import random
print(random.randint(1,100))

# import sys and find python path
import sys
for python in sys.path:
    print(python)

# install and uninstall package using pip (here camelcase is a sample package name)
# install - pip install camelcase
# uninstall - pip uninstall camelcase
