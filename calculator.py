num1=int(input("enter any first number"))
num2=int(input("enter any second number"))
op=input("choose operator symbol(+,-,*,/,%)")
if op == "+":
    print("The Sum is",num1+num2)
elif op== "-":
    print("The substraction is",num1-num2)
elif op== "*":
    print("The multiplication is",num1*num2)
elif op== "/":
    print("The division is",num1/num2) 
elif op== "%":
    print("The module is",num1%num2)     
     
else:
    print("choose right operator symbol")

