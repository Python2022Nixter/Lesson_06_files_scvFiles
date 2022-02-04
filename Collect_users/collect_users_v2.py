FILE_NAME = "users.txt"
# input name
name = input("Enter name: ")

# append to file
f = open(FILE_NAME, "a")
f.write(name + "\n")
f.close()
