# You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
# Names of people in the format "John Dow" first and second name. Find those who are on all blacklists.

casino_blacklist = {"John Dow", "Joseph Cooper", "Amelia Brand", "John Brand", "Fred Duggar"}
poker_blacklist = {"John Dow", "Will Dormer", "Ellie Burr", "Fred Duggar"}
alcohol_blacklist = {"John Dow", "Will Dormer", "Amelia Brand", "Fred Duggar"}

casino_poker = casino_blacklist.intersection(poker_blacklist)
all_blacklists = casino_poker.intersection(alcohol_blacklist)
print(all_blacklists)



