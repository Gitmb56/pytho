def build():
    def hello():
        return "hello freinds "
    ap = hello()
    return ap

if __name__ =="__main__":
    try:
        my = build()
        print(my)
    except Exception as e:
        print("Error: ",e)

