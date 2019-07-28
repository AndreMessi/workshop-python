import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

s

dates = pd.date_range('20130101', periods=6)

dates

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

df2

df2.types

df.head()

df.columns()

df.to_numpy()

df2.to_numpy()

df.describe()

df.T

