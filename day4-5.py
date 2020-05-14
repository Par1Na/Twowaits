# Twowaits
Twowaits Problem
from collections import Counter  

  

votes =['aman','ammy','amaan','amann','aaman','amu', 

    'ammu','amy','ammmyy','ammyy','aman','parna','naman']  

  
#Count the votes for persons and stores in the dictionary 

vote_count=Counter(votes) 

  
#Find the maximum number of votes 

max_votes=max(vote_count.values()) 

  
#Search for people having maximum votes and store in a list 

lst=[i for i in vote_count.keys() if vote_count[i]==max_votes] 

  
#Sort the list and print lexicographical smallest name 

print(sorted(lst)[0]) 
