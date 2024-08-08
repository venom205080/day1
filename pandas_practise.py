import pandas as pd
import numpy as np
s = pd.Series([1, 3, 5, 6, 8])

# print(s)
# df2 = pd.DataFrame(
#     {
#         "A": 1.0,
#         "B": pd.Timestamp("20130102"),
#         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
#         "D": np.array([3] * 4, dtype="int32"),
#         "E": pd.Categorical(["test", "train", "test", "train"]),
#         "F": "foo",
#     }
# )

# print(df2)

dates = pd.date_range("20130101", periods=6)
# cat = pd.Categorical(["test", "train", "test", "train"])
# print(cat)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=["a", "b", "c", "d"])
# print(df.head(2))
# print(df.tail(2))
# print(df)
# print(df.to_numpy())
# print(df.describe)

# print(df.T)

# print(df["a"])   #gives back particular column
# print(df[:3])     #gives back range of rows
# print(df["20130101": "20130104"])     #gives back ranges of rows
# print(df.loc[dates[1]])             #gives back matching row

# print(df.loc[: , ["a", "b"]])           #gives back matching column from a to b

# print(df.loc[dates[0], "a"])   #gives back dates[0] wali row me "a" column per data

# df.iloc[3]   # 3rd index(row) ka data

# df.iloc[3:5, 0:2]  # 3rd to 5th row and 0 to 2nd index ka data

# df[df["A"] > 0]   #Select rows where df.A is greater than 0.

# df2[df2["E"].isin(["two", "four"])]     #df2 me vo data show kro jha df2 ke E column me two ya four data h

# print(df[df > 0] )     #df me vo data dikhao jha df ke kisi b cell me value greater than 0 h baki jgh NaN fill ho jaega

# s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
# print(s1)

# setting values
# df.at["2013-01-01", "a"] = 0        #setting values by label
# df.at[dates[0], "a"] = 0        #setting values by label

# df.iat[0, 1] = 0        #setting value by position - 0th row and 1st col wali value ko 0 set krdo
# loc[rows, columns]
# df.loc[:, "D"] = np.array([5] * len(df))  # df me location jha pr bhi whole row and column is D wha apne aap smj jao

# df2[df2 > 0] = -df2      # df2 me jha b kisi b df2 ke cell me value 0 se bdi h vha usi value ko negative set krdo

# print(df)

# ----missing data-------
# missing data is represented by NaN
# DataFrame.dropna() -- drop the row that have missind data frame
# DataFrame.fillna(value)--fill the dataframe with given value

# isna()   -- is method se data frame me jha b nan hoga vha true baki jgh false show hoga