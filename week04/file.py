filename="HealthyPoint.txt"
try:
  f = open(filename,'r')
  print("Loading saved files ...")
  HP = f.readline()
except IOError:
  f = open(filename,'w')
  print("File not found ...")
  HP =f.readline()
if len(HP)== 0:
    HP=280

HP = int(HP)

if HP>280 or HP<=0:
    HP=280

t='Your current health is ' + repr(HP)
print(t)

point=""
while point!="quit":
    point=input('How much damage did you take?  ')
    if point=="quit":
        e="Health " + str(HP) + " has been stored."
        print(e)
        print("End")
        with open(filename,'w') as file_object:
            HP=str(HP)
            file_object.write(HP)
            file_object.close()
    else:
        HP=int(HP)-int(point)
        l = str(HP) + ' health left.'
        print(l)

    if int(HP)<=0:
        print("End")
        with open(filename,'w') as file_object:
            HP=str(HP)
            file_object.write(HP)
            file_object.close()
            break

