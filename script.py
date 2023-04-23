import pyam
import numpy as np
import matplotlib.pyplot as plt


#df = pyam.IamDataFrame(data='ar6_snapshot_1682174147.csv')
df = pyam.IamDataFrame(data='ar6_snapshot_1682242227.xlsx')
print(df)
df.filter(model='MESSAGE*').scenario

