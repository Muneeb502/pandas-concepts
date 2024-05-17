"""
in this file i make dataframe using pandas i  cnvert mydataset into dataframe    
    
"""

import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
