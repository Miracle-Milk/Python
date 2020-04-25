def Fib(num):
    i=0
    if num==0:
        return 0
    if num==1:
        return 1
    if num>=2:
        i=Fib(num-1)+Fib(num-2)
    return i
while True:
    number=int(input("Enter the N value of Fibonacci sequence F (N) : "))
    sum="F(" + str(number) +") = " + str(Fib(number))
    print(sum)