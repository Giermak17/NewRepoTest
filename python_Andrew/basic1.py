# Create variables to take input of two names.
name1 = input("What is your name? ")
name2 = input("What is your neighbor's name? ")
# create variables to take input of months.
time_coded1 = input("How many months have you been coding? ")
time_coded2 = input("And for you? ")
# add the total months
total_coded = int(time_coded1) + int(time_coded2)
# print the results
print("I am " + name1 + " and my neighbor is " + name2 + ".")
print("We have been coding for " + str(total_coded) + " months.")
