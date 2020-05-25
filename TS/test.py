from TS.test1 import arg
for x in range(0,1):
    for y in range(0,3):
      x1  = arg()
      x1.list.append(y)

x2=arg()
print(x2.list)
x2.list.clear()
print(x2.list)

