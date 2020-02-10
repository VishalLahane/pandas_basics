# pandas_basics

## data
https://github.com/tategallery/collection


### Two column with random numbers
```
import numpy as np 
import pandas as pd

# DataFrame is muti
my_first_df = pd.DataFrame(np.random.rand(3,2))   

# Single 
sp=pd.Series(np.random.rand(3),index=["first","second","third"])

```

### Examples
```
my_first_df.columns
Out[9]: RangeIndex(start=0, stop=2, step=1)

my_first_df.columns=["1","2"]

my_first_df
Out[11]: 
          1         2
0  0.134334  0.366762
1  0.942931  0.308785
2  0.861839  0.650761

my_first_df["1"]
Out[12]: 
0    0.134334
1    0.942931
2    0.861839
Name: 1, dtype: float64
```

### Pandas data can handle ( JSON,CSV)
- Text Files
- Binary files
- Database 




