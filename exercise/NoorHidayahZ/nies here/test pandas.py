import pandas as pd
# The standard way to import Pandas:
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

df = pd.read_csv('C:/Users/user/Desktop/GSE1456_lben.csv')
print(df.info())