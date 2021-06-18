#input two integers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
#adding the two numbers
sum = num1 + num2
print(sum)

#subtracting the two numbers
sub = num1 - num2
print(sub)

#division of two numbers
div = num1/num2
print(div)

#multiplication of two numbers
mul = num1*num2
print(mul)

#create a function by default values
def covid(patientname = 'Jo ' , bodytemperature = '98'):
    print( patientname + " " + 'has a body temperature of' + " " +  bodytemperature )

covid( patientname= 'John')
covid()
covid( patientname= 'Monica')
covid( patientname= 'Damon')
