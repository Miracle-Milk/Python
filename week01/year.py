## Global variable declaration ##
year = 0

## main code ##
if __name__ == "__main__" :
    year=int(input("input years : "))

if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)) :
    print("%d id leap year." % year);
else :
    print("%d is not leap year." % year);
