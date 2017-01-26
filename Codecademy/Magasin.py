# Exercise from Codecademy, initially on Python 2.7

total = 0                                            # create a variable used later

print( "Supermarket stocks: \n")

#price list
price = { "banana": 1.5,
"apple": 2,
"orange": 2,
"pear": 3 }

#stock list
stock = { "banana": 6,
"apple": 0,
"orange": 32,
"pear": 15 }

#------------------------------------------------------------
# print in a nice way the lists above :
#------------------------------------------------------------
 
for data in price and stock :                         # calls both lists, and will proceed every item/index from that list.
    print( "{}".format( data ) )                      #prints index
    print( "price : {} euros".format( price[data] ) ) #prints the data associated to the index in the said list: data[index]
    print( "stock : {}".format( stock[data] ) )       #same as above with list "stock"
	
    total_item = (price[data]) * (stock[data])        # total for the item currently proceeded
    print("Total value of {}s : {} euros".format( data, total_item ) )
    total += total_item                               # total for all items proceeded so far within the for loop
    print( )

print( "Total cost for all products : {} euros \n".format( total ) )

print( "Supermarket client: \n")

#------------------------------------------------------------
# calculate one client's bill according to products from a list :
#------------------------------------------------------------
def calculate_bill(food_list) :                       
    total = 0
    for fruit in food_list :
        if stock[fruit] > 0 :                         # doesn't count the item if out of stock
            total += price[fruit]
            stock[fruit] -= 1                         # remove one item from the supermarket's stocks
    return total                                      # result for the loop and function is returned
	
errands = ["banana", "banana", "banana", "orange", "orange", "apple"]

print( "Client bought: ", errands )
print( "Total expenses are {} euros \n".format( calculate_bill(errands) ) )       # function is applied to variable/list 'errands'

#------------------------------------------------------------
# changes after proceeding the client's shopping
#------------------------------------------------------------
print( "remaining stock:" )                                                    
for data in stock :
    print( "{}: {}".format( data, stock[data] ) )