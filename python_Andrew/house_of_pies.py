# create an order form
print = ("Welcome to the House of Pies! Here are our pies:")

# while we are still shopping
while shopping == "y":

    # shot pie selection prompt
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, (9) Tamale, (10) Steak")

    pie_choice = input("Which pie would you like? ")

    print("--------------")

    # get index of the pie from the selected number
    choice_index = int(pie_choice) - 1

    # add pie to the pie list by finding the matching index and adding one to its value
    pie_purchases.append(pie_choice) += 1
    print("----------------")

    # inform the customer of the pie purchase
    print("Great! We'll have that " + pie_list[choice_index] + "right out. "))

    # provide exit option
    shopping = input("Would you like to make another purchase?: (y)es or (n)o")

# Once the pie list is complete
print("----------------")

# Count instances of each pie
print("You purchased: ")

# loop through the full pie list
for pie_index in range(len(pie_list))