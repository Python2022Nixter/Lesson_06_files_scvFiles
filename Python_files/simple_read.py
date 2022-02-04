FILE_NAME = "first_test_file.txt"
f = open(FILE_NAME) # "r" is default
print(f.read())
f.close()