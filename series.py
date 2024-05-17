"""
in this file i give serial number what ever i want like the eample is given below

 """

import pandas as pd


lis = ["MUNEEB","AFZAAL","MOIZ","UBAID","OKASHA","HUXAIFA","ZAIN","PLUMBER","MASOOD","ARFA"]

mydata = pd.Series(lis , index=[ i for i in range(1,len(lis)+1)])

print(mydata)