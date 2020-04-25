
x=input('Please Ender the number:')
xlist=x.split(" ")
print(xlist)
xlist = [int(xlist[i]) for i in range(len(xlist))]      #for循环，把每个字符转成int值
print(xlist)
s='The maximum value in the list is: '+ repr(max(xlist))
print(s)
y='The minimum value in the list is:  '+ repr(min(xlist))   #repr()： 产生一个解释器易读的表达形式
print(y)