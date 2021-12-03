#!/usr/bin/env python3

#import pandas as pd

print("hello world")

released = {
		"iphone" : 2007,
		"iphone 3G" : 2008,
		"iphone 3GS" : 2009,
		"iphone 4" : 2010,
		"iphone 4S" : 2011,
		"iphone 5" : 2012
	}
print released

release1 = released.get("iphone", "none")
release2 = released.get("iphone 3G", "none")
release3 = released.get("iphone 3GS", "none")
release4 = released.get("iphone 4", "none")
release5 = released.get("iphone 4S", "none")
release6 = released.get("iphone 5", "none")

print release1
print release2
print release3
print release4
print release5
print release6


print("oldest release = " + str(released.get("none", "2007")))

# Let's try and save something in an array (think of it as a table)

#df1 = pd.DataFrame({'Name': ['Pankaj', 'Lisa'], 'ID': [1, 2]})
#df2 = pd.DataFrame({'Name': ['David'], 'ID': [3]})
#df3 = pd.DataFrame({'Name': ['Marcus'], 'ID': [4]})
#df4 = pd.DataFrame({'Name': ['Filip'], 'ID': [5]})

#print("********************** df1 = ")
#print(df1)


#print("********************** df2 = ")
#print(df2)

#df5 = df1.append(df2).append(df3).append(df4)
#df5.reset_index(drop=True, inplace=True)

#print('\nResult DataFrame:\n', df5)

# print(my_table)

# my_table.append("col1" : "a", "col2" : "b")

# print(my_table)
