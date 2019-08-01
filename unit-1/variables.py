
'''
#integer aka whole numbers
age = 24

#float aka decimals 
gpa = 3.0 

#boolean aka TRUE OR FALSE (must be spelled with capital first letter)
has_kids = True

#check the type of variable
print(type(age))
print(type(gpa))
print(type(has_kids))

# Check if a number is even or odd
# when we write an if statement we are creating a block which is why we have ":"

num = 10
if num % 2 == 0: 
    print('It is even!')
else:
    print ('It is odd!')

#comparison operators 
# > - greater than
# < - less than
# >= - greater than or equal to 
# <= less than or equal to 
# == - equal to 
# ! - not equal to 

#Truthiness '''
x = 10 # a none zero value is TRUTHY....however if it is 0 or negative...it's gunna be FALSEY

y = 0 #zero or negative value is Falsey

z = 'Python' # a string of non 0 length is TRUTHY

p = '' # a string of 0 length is FALSEY

q = [] # an empty listi s FALSEY

if q:
    print('yes')
else: 
    print ('no')


