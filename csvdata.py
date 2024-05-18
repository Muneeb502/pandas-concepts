import pandas as pd

print("in this file i ma going to understand the basic condets of csv file")


df = pd.read_csv("CSV-FILECSV.csv")

## find the shpe of  data means   find the numbers of raw and numbers of colunms
print("find the shpe of  data means   find the numbers of raw and numbers of colunms")

print(df.shape)

## find the info of  data means  it will show me the numbers of colums and raw and also data type 
print("find the info of  data means  it will show me the numbers of colums and raw and also data type ")

print(df.info())