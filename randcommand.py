from random import *
import os
"""
generate a random command for each input file in "input"
and send the output to a corresponding filename in "output"

commands are of the form
../showgen -g 0 -a -tx 0,3 -ty 2,3 -wx 4,5 -wy 6,7
"""
files = os.listdir("input")
i = 0
for file in files:
  inp = file + " "
  outp = "output/" + inp

  random = Random()

  #seed all rands with i
  random.seed(i)
  i+=1

  exe = "../showgen "
  gen = ""
  a = ""
  tx = ""
  ty = ""
  wx = ""
  wy = ""

  if random.uniform(0,1) < 0.7:
    gen = "-g " + str(random.randint(0,1000)) + " "
  if random.choice([True, False]):
    a = "-a "
  if random.choice([True, False]):
    low = random.randint(-50,50)
    high = low + random.randint(0,50)
    tx = "-tx " + str(low) + "," + str(high) + " "
  if random.choice([True, False]):
    low = random.randint(-50,50)
    high = low + random.randint(0,50)
    ty = "-ty " + str(low) + "," + str(high) + " "
  if random.choice([True, False]):
    low = random.randint(-50,50)
    high = low + random.randint(0,50)
    wx = "-wx " + str(low) + "," + str(high) + " "
  if random.choice([True, False]):
    low = random.randint(-50,50)
    high = low + random.randint(0,50)
    wy = "-wy " + str(low) + "," + str(high) + " "

  command = exe + gen + a + tx + ty + wx + wy + inp + "> " + outp
  print command
  #os.system(command)