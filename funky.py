# make a program to get the average
def average(lst):
    return sum(lst)/len(lst)

lst = [3, 4, 5, 6, 7]
average = average(lst)

print("Average of the list =", round(average, 2))

