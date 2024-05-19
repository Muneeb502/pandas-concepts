import pandas as  pd
import numpy as np

dic = {
    "name": ["ali"],
           
    "age": [10], 

     "city": ["kasmir"]
}
##adding new item in list dictnoray

dic["name"].extend(["manzoor","bilal","moiz","afzaal","tariq","muneeb","usama","ubaid","arfa","zain","zuhaid"])

dic["age"].extend([20,56,12,45,23,22,21,28,21,34,35])

dic["city"].extend(["Karachi","Lahore","Faisalabad",'Rawalpindi','Gujranwala','Peshawar','Multan','Islamabad','Quetta','Bahawalpur',"gojra"])

##adding more col into data 


dic["courses"]= ['pyhton', 'webdevelopment' , 'datascience', 'pyhton ', 'GD' ,'fullter' , 'figma' , 'backenddevelpoer' , 'mernstack developer' , "data eng",'javasxript','java' ]

#print(len(dic["age"]))
#print(len(dic["name"]))
#print(len(dic["city"]))
#print(len(dic["courses"]))


"""
making dictnoary into dataframe wth the help of pandas 

 """

d = pd.DataFrame(dic)
print(d)

print(d.columns)

# arranged data col 
d.columns = [[ 'name', 'courses', 'city','age']]

print(d)