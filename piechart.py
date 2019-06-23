#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

# reading data from csv file
df = pd.read_csv('student.csv')

# piechart
plt.pie(df.iloc[0:,1],labels=df.iloc[0:,0],autopct='%1.1f%%')
plt.legend()
plt.show()

