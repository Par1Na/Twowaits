# Twowaits
Twowaits Problem

# Python code to demonstrate 
# for removing duplicate values from dictionary 

  
# initialising dictionary 

ini_dict = {'a':{'b':1, 'c':2}, 'b':{'b':1, 'c':2},  

            'c':{'a':2, 'b':3}, 'd':{'a':2, 'b':7}} 

  
# printing initial_dictionary 

print ("initial dictionary", str(ini_dict)) 

  
# code to remove duplicates 

result = {} 

  

for key, value in ini_dict.items(): 

    if value not in result.values(): 

        result[key] = value 

          
# printing result 

print ("result", str(result))
