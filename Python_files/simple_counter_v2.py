FILE_NAME = "counter.txt"

with open(FILE_NAME, "r+") as f:
    try:
        counter = int(f.read())
        counter += 1
        f.seek(0)
        f.write(str(counter))
    except:
        counter = 0
    
    print("Counter:", counter)
    pass
