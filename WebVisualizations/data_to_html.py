# Python program to convert 
# CSV to HTML Table 


import pandas as pd 

# to read csv file named "cities" 
a = pd.read_csv("cities.csv") 

# to save as html file 
# named as "Table" 
a.to_html("Table.html") 

# assign it to a 
# variable (string) 
data_table = a.to_html() 
