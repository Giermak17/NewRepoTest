# create a loop for all the candy
Candy_List = [
    "Snickers", 
    "Skittles", 
    "Hershey's", 
    "Starburst", 
    "Kit Kat", 
    "Swedish Fish", 
    "Milky Way", 
    "Twix", 
    "Nerds"]

# the number of candies the user can choose
Allowance = 5

# the list used to store all the candies
Candy_Cart = []

# Print all of the candies to the screen and the index in brackets
for Candy in Candy_List:
    print(f'[{str(Candy_List.index(Candy))}] {Candy}')

# Run through a loop which allows the user to choose which candies to buy
print("Which candy would you like to buy?")
for x in range(Allowance):
    Selected = input("Input the number of the candy you want: ")

    # add the candy at the index chosen to the candy_cart list
    Candy_Cart.append(Candy_List[int(Selected)])

# loop through the cart to say what was bought
print("I bought...")
for Candy in Candy_Cart:
    print(Candy)

