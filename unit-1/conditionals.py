'''num = 7 

if num > 4:
    print ('too high')
elif num < 3:
    print ('too low')
else:
        print ('just right')

# when we have a chain of elifs...only one is done at a time
#it does one..then done.. then the next.. then done.. then next.. then done 
# elifes means if the condition is satisifed.. it does not need to check the other conditions

#print corresonding letters for grades
# 80 - 100, 'A'
# 79 - 60, print 'B'
# 50 - 59, print 'C'
# #0 - 49 =, print 'F' 


#ALWAYS REMEMBER COLONS.. IF ITS THE LAST CONDITION.. JUST PUT ELSE..
grade = 55

if grade >= 80:
    print ('A')
elif grade >= 60:
    print ('B')
elif grade >= 50:
    print ('C')
else:
    print ('F')

    #fizzbuzz
    #for the first 50 integers
    #if it is a multiple of 3, print 'fizz'
    #if it is a multiple of 5, print 'buzz'
    #if its a multiple of 15, print 'fizzbuzz'
    #otherwise, just print the number 

for num in range(1,51):

    if num % 15 == 0:
        print ('fizzbuzz')
    elif num % 3 == 0: 
        print('fizz')
    elif num % 5 == 0:
        print ('buzz')
    else:
        print (num)

# if something falls into multiple categories... then order matters '''


name = 'Fizzbuzz'

if len(name) > 4:
    print ('longer than 4')

if len(name) > 6:
    print ('longer than 6')

