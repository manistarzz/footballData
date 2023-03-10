import numpy as np 
import pandas as pd

#A pandas DataFrame is a 2 dimensional data structure

#This is how we read in the file using read_csv
df=pd.read_csv('Refs.csv')

#head() is used to get the number of n rows
print(df.head())

#Now we can edit the colunms so that its more readable and easier to understand

df.columns = ['Date','HomeTeam','AwayTeam',
              'Referee','HomeFouls','AwayFouls',
              'TotalFouls','HomeYellows','AwayYellows',
              'TotalYellows', 'HomeReds','AwayReds','TotalReds']

print(df.head(2))

#len tells us how many rows in this case matches we have
print(len(df))

#The best way to give a summary of your dataset is to use the .describe() method
"""
Count~ how many values are there?
Mean~ what is the mean average? (Sum of values/count of values)
STD~  what is the standard deviation? This number describes how widely the group differs around the average. If we have a normal distribution, 68% of our values will be within one STD either side of the average.
Min~  the smallest value in our array
25%/50%/75%~  what value accounts for 25%/50%/75% of the data?
Max~ the highest value in our array
"""

print(df.describe())
"""
From analysing we can see we have between 3 and 4 yellows in a game and that the
away team are more likely to get more cards

"""
#We can now use this to look at referees individually
groupedRefs=df.groupby("Referee")

print(groupedRefs.describe()['TotalYellows'])

