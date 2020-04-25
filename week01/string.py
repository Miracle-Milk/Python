## Global variable declaration ##
inStr = ''

## main code ##
if __name__ == "__main__" :
    inStr = input('input string --->')

for i in range(len(inStr) - 1, -1, -1) :
    print('%c' % inStr[i], end = '')

