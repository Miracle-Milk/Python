def Calc(num1,num2,act="+"):
    if act=="+":
        print(num1+num2)
        return
    elif act=="-":
        print(num1-num2)
        return
    elif act=="*":
        print(num1*num2)
        return
    elif act=="/":
        if num2==0:
            print("Dividend cannot be zero")
            return
        else:
            print(num1/num2)
            return
    else:
        print("Wrong symbol")
        return

number1=int(input("Number1: "))
number2=int(input("Number2: "))
output1=Calc(number1,number2)
output2=Calc(number1,number2,"-")
output3=Calc(number1,number2,"^")

