import os

class equation:
  def commands():
    print("The commands are: \nequation.quadsolve() - For quadratic equations. \nequation.slopeint() - For slope-intercept equations. - NEW: May still have bugs, but works for right now :) \nequation.help() - Brings up the help page.")

  def quadsolve():
    import re
    printed = ""
    quadratic = input("Enter the quadratic equation: ")
    nospaces = re.sub("[^0-9-.*/()+x^=]", "", quadratic)
    if "=0" in nospaces:
      nospaces = nospaces.split("=0")
      nospaces = nospaces[0]
    if "x**2" in nospaces:
      a = nospaces.split("x**2")
    elif "x^2" in nospaces:
      a = nospaces.split("x^2")
    if a[0] == "":
      a[0] = "1"
    if "x" not in a[1]:
      b = 0
      c = re.sub("[^0-9-.*()/]", "", a[1])
      a = a[0]
    else:
      c = a[1].split("x")
      b = re.sub("[^0-9-.*()/]", "", c[0])
      if b == "":
        b = "1"
      elif b == "-":
        b = "-1"
      a = re.sub("[^0-9-.*()/]", "", a[0])
      c = re.sub("[^0-9-.*()/]", "", c[1])
    if "--" in c:
      c = re.sub("[^0-9.*()/]", "", c)
    try:
      a = float(a)
    except:
      if "/" in a:
        a = a.split("/")
        a = float(int(a[0]) / int(a[1]))
    try:
      b = float(b)
    except:
      if "/" in b:
        b = b.split("/")
        b = float(int(b[0]) / int(b[1]))
    try:
      c = float(c)
    except:
      if "/" in c:
        c = c.split("/")
        c = float(int(c[0]) / int(c[1]))
    try:
      x1p1 = -b
      x1p2 = b**2
      x1p3 = -4*(a*c)
      x1p4 = (x1p2 + x1p3)**0.5
      x1 = (x1p1 + x1p4)/(2*a)
      x2 = (x1p1 - x1p4)/(2*a)
    except:
      pass
    if str(type(x1)) == "<class 'complex'>":
      print("\nNo Solution (Negative Radical)")
      printed = True
    if x1 == x2:
      print("\nSolution:",x1)
    elif printed != True:
      print("\nSolution 1:",x1)
      print("Solution 2:",x2)
    
    
  def slopeint():
    import re
    yint = ""
    eq = input("Enter two points (ex. (1,-1),(2,-1) ): ")
    eq = eq.split(",")
    point1 = re.sub("[^0-9.-]","",eq[0])
    point2 = re.sub("[^0-9.-]","",eq[1])
    point3 = re.sub("[^0-9.-]","",eq[2])
    point4 = re.sub("[^0-9.-]","",eq[3])
    rise = float(point4) - float(point2)
    run = float(point3) - float(point1)
    if rise/run == 1.0:
      slope = 1
      calc = 0
    elif rise/run == -1.0:
      slope = -1
      calc = 0
    else:
      slope = rise/run
      calc = 1
    yint =  [float(point1),float(point2)]
    if calc == 0:
      if float(point1) != 0:
        yint[0] -= float(point1)
        yint[1] -= float(point1)
    elif calc == 1:
      start = [0,0]
      for i in range(5):
        start[1] -= 0.01
        slope2 = float(point3) - start[0]/float(point4) - start[1]
        if slope == slope2:
          break
        slope2 = -1*slope2
        if slope == slope2:
          break
        slope2 = -1*slope2
    if yint == [0.0,0.0]:
      if calc == 0:
        print(f"y = {slope}x")
      elif run == -1.0:
        print(f"y = {-1*rise}x")
      else:
        print(f"y = {rise}/{run}x")
    elif calc == 0:
      if yint[1] > 0:
        print(f"y = {slope}x + {yint[1]}")
      elif yint[1] < 0:
        print(f"y = {slope}x {yint[1]}")
    elif run == -1.0:
      if yint[1] > 0:
        print(f"y = {-1*rise}x + {yint[1]}")
      elif yint[1] < 0:
        print(f"y = {-1*rise}x {yint[1]}")
    else:
      if yint[1] > 0:
        print(f"y = {rise}/{run}x + {yint[1]}")
      elif yint[1] < 0:
        print(f"y = {rise}/{run}x {yint[1]}")
    
if "__name__" == "__eqsolvecarlover101__":
  equation.quadsolve()
  equation.slopeint()
  equation.commands()

os.system("clear")
print("Type equation.commands() to get started or click on 'Code' to read the README.md file for for information.")
