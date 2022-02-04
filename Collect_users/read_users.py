FILE_NAME = "users.txt"
OUT_FILE = "result.txt"


f = open(FILE_NAME)
from_file = f.read()
f.close()
users = from_file.split("\n")
print(users)

# 

f = open(FILE_NAME)
users = f.readlines()
print(users)

# 

for i in range(len(users)):
    if len(users[i]) <= 3:
        del(users[i])      # not working !!!!!


f = open(OUT_FILE, "w")
f.writelines(users)
f.close()
