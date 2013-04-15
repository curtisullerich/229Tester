#generates random .aut files
from random import *
import string, sys, os, errno
def mkdir_p(path):
  try:
    os.makedirs(path)
  except OSError as exc: # Python >2.5
    if exc.errno == errno.EEXIST and os.path.isdir(path):
      pass
    else: raise


n = 100;

if (len(sys.argv)!=3):
  print "usage: python fuzzy.py testdir execdir"
  sys.exit(0)

testdir = sys.argv[1]
execdir = sys.argv[2]

mkdir_p(testdir)
mkdir_p(testdir+"/generatedaut")
mkdir_p(testdir+"/oracleinput")
mkdir_p(testdir+"/oracleoutput")
mkdir_p(testdir+"/showgenoutput")


for i in range(1):
  random = Random()
  random.seed(i)
  """
  commands are of the form
  ./showgen -g 0 -a -tx 0,3 -ty 2,3 -wx 4,5 -wy 6,7
  """
  exe = execdir + "/showgen "
  gen = ""
  a = ""
  tx = ""
  ty = ""
  wx = ""
  wy = ""

  fname = "test" + str(i) + ".aut"
  wxLow = None
  wxHigh = None
  wyLow = None
  wyHigh = None
  xLow = None
  yLow = None
  runToGen = 0

  if random.uniform(0,1) < 0.7:
    runToGen = random.randint(0,1000)
    gen = "-g " + str(runToGen) + " "
  if random.choice([True, False]):
    a = "-a "
  if random.choice([True, False]):
    xLow = random.randint(-50,50)
    xHigh = xLow + random.randint(0,50)
    tx = "-tx " + str(xLow) + "," + str(xHigh) + " "
  if random.choice([True, False]):
    yLow = random.randint(-50,50)
    yHigh = yLow + random.randint(0,50)
    ty = "-ty " + str(yLow) + "," + str(yHigh) + " "
  if random.choice([True, False]):
    wxLow = random.randint(-50,50)
    wxHigh = wxLow + random.randint(0,50)
    wx = "-wx " + str(wxLow) + "," + str(wxHigh) + " "
  if random.choice([True, False]):
    wyLow = random.randint(-50,50)
    wyHigh = wyLow + random.randint(0,50)
    wy = "-wy " + str(wyLow) + "," + str(wyHigh) + " "

  command = exe + gen + a + tx + ty + wx + wy 
  if (random.choice([True,False])):
    command += " < " #to read as stdin instead of file
  command += testdir + "/generatedaut/" + fname

  if a != "":
    command += " | " + exe 
  command += " > " + testdir + "/showgenoutput/test" + str(i) + ".229"


  """ I DO WHAT I WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANT """

  autxLow = random.randint(-50,50)
  autxHigh = random.randint(-50,50)
  if(autxLow > autxHigh):
    tmp = autxLow
    autxLow = autxHigh
    autxHigh = tmp

  autyLow = random.randint(-50,50)
  autyHigh = random.randint(-50,50)
  if(autyLow > autyHigh):
    tmp = autyLow
    autyLow = autyHigh
    autyHigh = tmp

  if(xLow == None):
      xLow = autxLow
      xHigh = autxHigh

  if(yLow == None):
      yLow = autyLow
      yHigh = autyHigh

  f = open(testdir + "/generatedaut/" + fname, "w")
  f.write("Xrange " + str(autxLow) + " " + str(autxHigh) + ";\n")
  f.write("Yrange " + str(autyLow) + " " + str(autyHigh) + ";\n")

  f.write('Name "Generated by Ryan mwahaha";\n')

  rd = random.randint(0,255)
  gd = random.randint(0,255)
  bd = random.randint(0,255)
  ra = random.randint(0,255)
  ga = random.randint(0,255)
  ba = random.randint(0,255)

  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  liveChar = random.choice(chars)
  deadChar = random.choice(chars)
  f.write("Colors (" + str(rd) + ", " + str(gd) + ", " + str(bd) + "), (" + str(ra) + ", " + str(ga) + ", " + str(ba) + ");\n")
  f.write("Chars " + deadChar + ", " + liveChar + ";\n")

  f.write("Initial {\n")
  firstX = True
  yList = range(autyLow, autyHigh+1)
  #random.shuffle(yList)
  oracleList = [[]]
  for y in yList:
    xList = range(autxLow, autxHigh+1)
    if(random.choice([True,False])):
      f.write("Y = " + str(y) + " : ")
      #random.shuffle(xList)
      for x in xList:
        #also print input stuff for 308 program
        if(random.choice([True,False])):
          if(yLow <= y and y <= yHigh and xLow <= x and x <= xHigh):
              oracleList[y-yLow][x-xLow] = 1
          if (firstX):
            f.write(str(x))
            firstX = False
          else:
            f.write("," + str(x))
        else:
          if(yLow <= y and y <= yHigh and xLow <= x and x <= xHigh):
              oracleList[y-yLow][x-xLow] = 0
      f.write(";\n")
      firstX = True
    else:
      for x in xList:
          if(yLow <= y and y <= yHigh and xLow <= x and x <= xHigh):
              oracleList[y-yLow][x-xLow] = 0
  f.write("};\n")

  """ using command from above!"""
  if (wxLow is None):
    wxLow = xLow
  if (wxHigh is None):
    wxHigh = xHigh
  if (wyLow is None):
    wyLow = yLow
  if (wyHigh is None):
    wyHigh = yHigh

  print command
  os.system(command)

  #we know ranges here
  #xLow, xHigh, yLow, yHigh
  #wxLow, wxHigh, wyLow, wyHigh

  #generate oracle
  for genNum in range(0,runToGen):
    tmp = oracleList[:][:]
    for y in range(0,yHigh-yLow):
      for x in range(0,xHigh-xLow):
        liveNeighbors = 0
        i = y-1
        j = x-1
        while(i <= y+1):
          while(j <= j+1):
            if(yLow <= i and i <= yHigh):
              if(xLow <= j and j <= xHigh):
                if(oracleList[i][j] == 1 and i != x and j != y):
                  liveNeighbors += 1
        if(oracleList[y][x] == 1):
          if(liveNeighbors == 2 or liveNeighbors == 3):
            tmp[y][x] = 1
          else:
            tmp[y][x] = 0
        elif(oracleList[y][x] == 0):
          if(liveNeighbors == 3):
            tmp[y][x] = 1
          else:
            tmp[y][x] = 0
    oracleList = tmp[:][:]

  #crop and diff

  testF = open("showgenoutput/test" + str(i) + ".229")
  testPassed = True
  for y in range(wyLow-yLow, (wyLow-yLow)+(wyHigh-wyLow)+1):
    for x in range(wxLow-xLow, (wxLow-xLow)+(wxHigh-wxLow)+1):
      cell = testF.read(1)
      if((cell != liveChar and oracleList[y][x] == '1')):
        testPassed = False
        print "Test " + str(i) + " failed at window index ("+str(x)+","+str(y)+")"
      elif((cell != deadChar and oracleList[y][x] == '0')):
        testPassed = False
        print "Test " + str(i) + " failed at window index ("+str(x)+","+str(y)+")"
    returnStatement = testF.read(1)
    if(returnStatement != '\n'):
      testPassed = False
      print "Test " + str(i) + " failed at y=" + str(y) + "with no return statement"

  if(testPassed):
      print "Test " + str(i) + " passed!"
    

