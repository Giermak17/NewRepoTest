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

# Print all the candies and their index in brackets
for i in range(len(Candy_List)):
    print("[" + str(i) + "]" + Candy_List[i])

# set answer to "yes" for while loop
answer = "yes"
while answer == "yes":
    
    # ask which candy the user wants to buy
    print("Which candy would you like to buy?")
    Selected = input("Input the number of the candy you want: ")

    # add the candy at the index chosen to the candy_cart list
    Candy_Cart.append(Candy_List[int(Selected)])

    # ask if they want more candy
    answer = input("Would you like to make another selection? ('yes' or 'no' ")

# loop through the cart to say what was bought
print("I bought...")
for Candy in Candy_Cart:
    print(Candy)

