"""
in this file i am going to calling data in raw using mthod and also adding myown serial number using series

"""
import pandas as pd
## creating different list in  dictonary
mydic ={ 
"id" :['1a', '2b', '3c'],
"name" :['Anna', 'Peter', 'John'],
"year" :  [1999, 2001, 1993]
}

mydata = pd.DataFrame(mydic , index=[a for a in range(1,len(mydic)+1)] )

print(mydata)

print("===================calling data from raw  multiple raw===========================")


print(mydata.loc[[1,2]])

print("===================calling data from raw single raw===========================")

print(mydata.loc[3])
