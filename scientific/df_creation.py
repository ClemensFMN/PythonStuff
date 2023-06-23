# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:55:01 2023

@author: 700001473
"""

import pandas as pd
import numpy as np

# simplest case is to create df from a dict[string:array] where the string gives the column name
# the index implicitely starts at 0
d = {"one": [1.0, 2.0, 3.0, 4.0], "two": [4.0, 3.0, 2.0, 1.0]}
df = pd.DataFrame(d)


# a bit more advanced: two series each provided with an index
# the indices do not overlap, and the resulting df "aligns" them correctly; missing values are set to NaN
d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}

df = pd.DataFrame(d)


# the same works for date/times as well
date1 = pd.date_range("2013-01-01", periods=6)
date2 = pd.date_range("2013-01-04", periods=6)

d = {
    "one": pd.Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], index=date1),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], index=date2),
}

df = pd.DataFrame(d)

