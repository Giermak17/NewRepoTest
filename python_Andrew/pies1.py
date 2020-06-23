# initial variable to track shopping status
shopping = 'y'
# List to track pie purchases
pie_purchases = []
# make pie list
pie_list = ["Pecan", "Apple", "Bean", "Banoffee", "Rhubarb", "Blueberry", "Peach", "Tamale", "Steak", "Chocolate"]
# display initial message
print("Welcome to the House of Pies! Here are our pies:")
# while we are still shopping...
while shopping == "y":

    # Show pie selection prompt
    print("(1) Peach, (2) Apple, (3) Bean, (4) Banoffee, (5) Rhubarb, (6) Blueberry, (7) Peach, (8) Tamale, (9) Steak, (10) Chocolate ")
    pie_choice = input("Which would you like? ")
    # add pie to pie list
    pie_purchases.append(pie_choice)

    # inform the customer of the pie purchase
    print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " right out. Thank you.")
    # provide exit option
    shopping = input("Would you like to make another purchase: (y)es or (n)o ")

# Once the pie list is complete
print("You purchased a total of " + str(len(pie_purchases)) + ".")
