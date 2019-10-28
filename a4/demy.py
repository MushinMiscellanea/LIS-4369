import re
import numpy as np
import pandas as pd
#np.set_printoptions(threshold=np.inf)

def requirements():
    print('requirements')

def data_analysis():

    np.set_printoptions(threshold=np.inf) 
    url = "https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/Stat2Data/Titanic.csv"

                                # read_csv panda method to read the csv
    df = pd.read_csv(url)

    print('DataFrames composed of three components: index, columns, and data. Data also known as values')
    index = df.index
    columns = df.columns
    values = df.values

    #print indexes
    print(index)

    #print columns 
    print(columns)

    #alternative way to print columns
    print(df.columns[:])

    #print all values in array format
    print(values)

    #print component datatypes
    print(type(index))
    print(type(columns))
    print(type(values))


    #print DataFrame information
    print(df.info())

    #print first 5 rows
    print(df.head())

    #drop first row
    df = df.drop('Unnamed: 0', 1)

    #print info and head
    print(df.info())

    print(df.head())

    #precise data selection
    # df.iloc[[rows],[columns]]
    print('DataFrame data slicing using .loc and .iloc')
    print(df.iloc[:3])   #slice notation is [start, stop, step]

    print(df.iloc[1310:])   #iloc gets data from integer indexes. loc gets data from given names

    # select specific rows and columns
    a= df.iloc[[0,2,4], [1,3,5]]
    print(a)

    a = df.iloc[:,[1,3,5]]
    print(a)
    a = df.iloc[[0,2,4], :]
    print(a)

    #print all rows and columns
    a = df.iloc[:, :]
    print(a)
    #print rows starting at second row (index at 1)
    a = df.iloc[:, 1:]
    print(a)

    a = df.iloc[0:1, 0:1]
    print(a)

    a = df.iloc[2:5, 2:5]
    print(a)

    b = df.iloc[:, 1:].values
    print(type(df))
    print(type(a))
    print(type(b))
    print(b.shape)
    print(b.dtype)
    print(a)
    print(len(a))
    print(b)
    print(len(b))
     #print elements in second row third column in array
    print(b[1,2])

    names = df['Name']
    print(names)

    #start using regular expression commands

    for name in names:
        i = re.search(r'(Allison)', name)
    print(i)
    # start comparing values

    #print mean age
    avg = df['Age'].mean()
    print(avg)

    #print mean age rounded to 2 decimals
    avg = df['Age'].mean().round(2)
    print(avg)

    #print mean of every column

    avg_all = df.mean(axis=0)
    print(avg_all)

    #print summary statistics
    describe = df['Age'].describe()
    print(describe)

    #print min, max, median and mode age

    min = df['Age'].min()
    print(min)

    max = df['Age'].max()
    print(max)

    median = df['Age'].median()
    print(median)

    mode = df['Age'].mode()
    print(mode)

    #print number of values in column
    num = df['Age'].count()
    print(num)

    print()
    print('time to graph')

    df.Age[0:20].plot()

def main():
    requirements()
    data_analysis()

if __name__ == "__main__":
    pass
