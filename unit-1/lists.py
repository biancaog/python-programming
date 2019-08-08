classmates = ['Connor', 'Efe', 'Alexander', 'Bianca', 'Edwin', 'Greg']

'''#print a l ist
print(classmates)

#numberof items in a list... you use the function len
print(len(classmates))

#get a specific item in a list - for example, the first item
print(classmates[0])

#get a specific item in a list - for example, the last iteam
print(classmates[len(classmates)-1])
#the last item will always be the length -1

#shortcut to get the last element
print(classmates[-1])

#slicing - taking sections of the list **important when you do data science***
print(classmates[0:3])

#adding an element to the end of a list aka APPEND
classmates.append('Princeton')
print(classmates)

#remove from end of list aka POP
classmates.pop()

print(classmates)

#inserting at a specific position aka INSERT
classmates.insert(0, 'Princeton')
print(classmates)

#removing an element from a specific position aka REMOVE
classmates.remove('Princeton')
print(classmates)'''


#calculate the sum of a list of numbers
ages = [15, 25, 30, 27, 29, 41, 23, 20, 31, 19]

#use a for loop
total_ages = 0
'''for age in ages:
    total_ages += age #+= takes total_ages, and each time, we are reassigning the value to the sum of the old total_ages, += means UPDATING THE OLD VALUE 

print(total_ages)
#another for loop - use range and indexes
for idx in range(len(ages)):
    total_ages += ages[idx]
print(total_ages)'''

#print(sum(ages))

#calculate the sum of all the odd number ages in the list 

for age in ages:
    if age % 2 == 1:
        total_ages += ages

print(total_ages)