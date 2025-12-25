from sub import subt
from addi import add1

#for i in range(0,11):
i = 6
if i>5:
    print("additional fun calling........ ")
    on = int(input("additional Enter a number:  "))
    no =int(input("additional Enter a number: "))
    print(add1(on,no))
else:
    print("subtraction fun calling...........")
    print(subt(5,4))

