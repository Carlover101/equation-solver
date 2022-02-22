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
    elif rise == 0:
      slope = "x"
      calc = -1
    else:
      slope = rise/run
      calc = 1
    if calc == -1:
      yint = 0
    elif calc == 0:
      if float(point1) != 0:
        yint -= float(point1)
    elif calc == 1:
      number = float(point4)
      number2 = 0.01
      number3 = slope
      number4 = float(point3)
      divider = 0
      status = None
      if number > 0:
        if number4 < 0:
          while True:
            if (number-number2)/number4 == number3:
              break
            elif (number-number2)/number4 < number3:
              if status != "smaller":
                status = "smaller"
                divider += 1
              number2 = number2 + (1 / (divider*10))
              number2 = round(number2,divider+1)
            elif (number-number2)/number4 > number3:
              if status != "larger":
                status = "larger"
                divider += 1
              number2 = number2 - (1 / (divider*10))
              number2 = round(number2,divider+1)
        elif number4 > 0:
          while True:
            if (number-number2)/number4 == number3:
              break
            elif (number-number2)/number4 < number3:
              if status != "smaller":
                status = "smaller"
                divider += 1
              number2 = number2 - (1 / (divider*10))
              number2 = round(number2,divider+1)
            elif (number-number2)/number4 > number3:
              if status != "larger":
                status = "larger"
                divider += 1
              number2 = number2 + (1 / (divider*10))
              number2 = round(number2,divider+1)
      elif number < 0:
        if number4 > 0:
          while True:
            if (number-number2)/number4 == number3:
              break
            elif (number-number2)/number4 < number3:
              if status != "smaller":
                status = "smaller"
                divider += 1
              number2 = number2 + (1 / (divider*10))
              number2 = round(number2,divider+1)
            elif (number-number2)/number4 > number3:
              if status != "larger":
                status = "larger"
                divider += 1
              number2 = number2 - (1 / (divider*10))
              number2 = round(number2,divider+1)
        elif number4 > 0:
          while True:
            if (number-number2)/number4 == number3:
              break
            elif (number-number2)/number4 < number3:
              if status != "smaller":
                status = "smaller"
                divider += 1
              number2 = number2 - (1 / (divider*10))
              number2 = round(number2,divider+1)
            elif (number-number2)/number4 > number3:
              if status != "larger":
                status = "larger"
                divider += 1
              number2 = number2 + (1 / (divider*10))
              number2 = round(number2,divider+1)
      yint = round(number2,1)
    if calc == -1:
      print(f"y = {point4}")
    elif yint == 0:
      if calc == 0:
        print(f"y = {slope}x")
      elif run == -1.0:
        print(f"y = {-1*rise}x")
      else:
        if rise % run == 0:
          print(f"y = {rise/run}/{run/run}x")
        elif run % rise == run / 0.5:
          print(f"y = {rise/rise}/{run/rise}")
        else:
          print(f"y = {rise}/{run}")
    elif calc == 0:
      if yint > 0:
        print(f"y = {slope}x + {yint}")
      elif yint < 0:
        print(f"y = {slope}x {yint}")
    elif run == -1.0:
      if yint > 0:
        print(f"y = {-1*rise}x + {yint}")
      elif yint < 0:
        print(f"y = {-1*rise}x {yint}")
    else:
      if yint > 0:
        print(f"y = {rise}/{run}x + {yint}")
      elif yint < 0:
        print(f"y = {rise}/{run}x {yint}")

  def perpint():
    import re
    eq = input("Enter the slope of the first line ( ex. 1/2x ): ")
    intsec = input("Enter the point of intersection ( ex. (1,2) ): ")
    opp = eq.replace("[^0-9/.-]","")
    opp = opp.split("/","")
    opp[0],opp[1] = int(opp[0]),int(opp[1])
    opp2 = -1*(opp[1]) / opp[0]

  def midpoint():
    import re
    points = input("Enter two points. ( ex. (-1,2),(1,-2) ): ")
    points = points.split(",")
    point1 = int(re.sub("[^0-9.-]","",points[0]))
    point2 = int(re.sub("[^0-9.-]","",points[1]))
    point3 = int(re.sub("[^0-9.-]","",points[2]))
    point4 = int(re.sub("[^0-9.-]","",points[3]))
    print(f"Midpoint: ({(point1 + point3)/2},{(point2 + point4)/2})")

os.system("clear")
print("Type equation.commands() to get started or click on 'Code' to read the README.md file for for information.")
