'''Write code that classifies a given amount of money (which you store in a
variable named amount), specified in cents, as greater monetary units. Your code lists the
monetary equivalent in dollars (100 ct), quarters (25 ct), dimes (10 ct), nickels (5 ct), and
pennies (1 ct). Your program should report the maximum number of dollars that fit in the
amount, then the maximum number of quarters that fit in the remainder after you subtract
the dollars, then the maximum number of dimes that fit in the remainder after you subtract
the dollars and quarters, and so on for nickels and pennies. The result is that you express
the amount as the minimum number of coins needed.'''

from pcinput import getInteger

DOLLARS = 100
QUARTERS = 25
DIMES = 10
NICKELS = 5
PENNIES = 1

amount = getInteger( "How much must be returned? " )

dollars_bills = amount // DOLLARS
amount %= DOLLARS
quarters_coins = amount // QUARTERS
amount %= QUARTERS
dimes_coins = amount // DIMES
amount %= DIMES
nickels_coins = amount // NICKELS
amount %= NICKELS
pennies_coins = amount // PENNIES


print( "The number of coins needed are:",
	dollars_bills , "dollars,",
	quarters_coins , "quarters,",
	dimes_coins , "dimes,",
	nickels_coins , "nickels and",
	pennies_coins, "pennies." )





