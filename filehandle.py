with open("char.txt","a") as f:
    for num in range(32,128):
        c = chr(num)
        f.write(c + "\n")
# file ka output dekhna hai 
with open("char.txt","r") as f:
    print(f.read())


