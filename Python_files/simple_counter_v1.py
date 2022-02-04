FILE_NAME = "counter.txt"

with open(FILE_NAME) as f:
    try:
        counter = int(f.read())
    except:
        counter = 0
    counter += 1
    print("Counter:", counter)
    pass
with open(FILE_NAME, "w") as f:
    f.write(str(counter))
    pass
