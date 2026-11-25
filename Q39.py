count = 0

def increment():
    global count
    count += 1
    print("Count inside:", count)

increment()
print("Count outside:", count)
