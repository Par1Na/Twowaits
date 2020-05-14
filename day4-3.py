# Twowaits
Twowaits Problem

# Python code to find second largest 
# element from a dictionary using sorted() method 

  
# creating a new Dictionary 

example_dict ={"a":13, "b":3, "c":6, "d":11} 

  
# now directly print the second largest 
# value in the dictionary 

print(list(sorted(example_dict.values()))[-2])
