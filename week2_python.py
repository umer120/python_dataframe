import numpy as np
import pandas as pd

data = np.array([
    ['Ali',25,'Lahore'],
    ['Sara',30,'Karachi'],
    ['Ahmed',22,'Islamabad']
])

df = pd.DataFrame(data,columns=['Name','Age','City'])
print(df)
