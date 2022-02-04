FILE_NAME = "users.txt"

f = open(FILE_NAME, "a")
next_user = " "
while len(next_user) != 0:
    next_user = input("Enter the next user: ")

    if input("Do you want to continue? (y/n) ") == "n": 
        f.write(next_user + "\n")

        break
    pass

f.close()




