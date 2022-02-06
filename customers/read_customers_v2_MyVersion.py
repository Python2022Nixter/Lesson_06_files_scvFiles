CUSTOMERS_FILE = "customers/customers.csv"
titles = []
coustomers =[]

# function for separate the string by ";"
def separate_string(string):
    lst = string.split(";")
    return lst
# function for print the list
def print_list(lst):
    for i in range(len(lst)):
        if len(titles[i]) <= 5:
            print(f"{titles[i]}: \t\t\t {lst[i]}")
        else:
            print(f"{titles[i]}: \t\t {lst[i]}")
        

# Open the file for reading
f  = open(CUSTOMERS_FILE, "r")
titles = separate_string(f.readline())
print(f"Search by: {titles[1]}")

# Loop customers.csv 
coustomers = f.readlines()
name = input("Enter the name: ").lower()

# find by name
for i in coustomers:
    lst = separate_string(i)
    if name in lst[1].lower():
        print_list(lst)
f.close()
#