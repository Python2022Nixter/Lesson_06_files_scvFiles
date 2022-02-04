CUSTOMERS_FILE = "customers/customers.csv"

# function for separate the string by ";"
def separate_string(string):
    lst = string.split(";")
    return lst

# Open the file for reading
f  = open(CUSTOMERS_FILE, "r")
print( separate_string(f.readline()) )
# Loop customers.csv 

# find by name

#