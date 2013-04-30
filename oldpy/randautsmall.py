#generates random .aut files
from random import *
import string
import sys
import os

if(len(sys.argv) == 1):
    print "This requires one argument: The probability with which each cell is alive in generation 0."
    sys.exit(1)

th = float(sys.argv[1])

random = Random()
random.seed(1)

xLow = random.randint(-50,50)
xHigh = random.randint(-50,50)
if(xLow > xHigh):
    tmp = xLow
    xLow = xHigh
    xHigh = tmp

yLow = random.randint(-50,50)
yHigh = random.randint(-50,50)
if(yLow > yHigh):
    tmp = yLow
    yLow = yHigh
    yHigh = tmp

print("Xrange " + str(xLow) + " " + str(xHigh) + ";\n")
print("Yrange " + str(yLow) + " " + str(yHigh) + ";\n")
print('Name "T;H;I;S; ;I;S; ;M;Y; ;N;A;M;E;";\n')

rd = random.randint(0,255)
gd = random.randint(0,255)
bd = random.randint(0,255) 
ra = random.randint(0,255) 
ga = random.randint(0,255) 
ba = random.randint(0,255) 
     
print("Colors (" + str(rd) + ", " + str(gd) + ", " + str(bd) + "), (" + str(ra) + ", " + str(ga) + ", " + str(ba) + ");\n")
#print("Chars " + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) + 
#                   ", " + 
#                   random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
#                   + ";\n")
print("Chars  ,*;")
print("Initial {\n")
firstX = True
yList = range(yLow, yHigh+1)
#random.shuffle(yList)
for y in yList:
  if(random.choice([True,False]) or True):
    sys.stdout.write("Y = " + str(y) + " : ")
    xList = range(xLow, xHigh+1)
    #random.shuffle(xList)
    for x in xList: 
      #also print input stuff for 308 program
      if(firstX):
        sys.stdout.write(str(x))
        firstX = False
      elif(random.uniform(0,1) < th):
        sys.stdout.write("," + str(x))
    print(";\n")
    firstX = True
print("};\n")
