class equation:
  def qsolv():
    printed = ""
    quadratic = input("Enter the quadratic equation: ")
    if "x**2" in quadratic:
      a = quadratic.split("x**2")
    elif "x^2" in quadratic:
      a = quadratic.split("x^2")
    b = a[1].split("x")
    if " + " in b[1]:
      c = b[1].split(" + ")
      c = int(c[1])
    elif " - " in b[1]:
      c = b[1].split(" ")
      c = int(-1 * int(c[2]))
    elif "+" in b[1]:
      c = b[1].split(" +")
      c = int(c[1])
    elif "-" in b[1]:
      c = b[1].split(" ")
      c = int(c[1])
    if " + " in b[0]:
      b = b[0].split(" + ")
      b = int(b[1])
    elif " - " in b[0]:
      b = b[0].split(" ")
      b = int(-1 * int(b[2]))
    elif "+" in b[0]:
      b = b[0].split(" +")
      b = int(b[1])
    elif "-" in b[0]:
      b = b[0].split(" ")
      b = int(b[1])
    if a[0] == "":
      a = int(1)
    else:
      a = int(a[0])
    try:
      x1p1 = -b
      x1p2 = b**2
      x1p3 = -4*(a*c)
      x1p4 = (x1p2 + x1p3)**0.5
      x1 = (x1p1 + x1p4)/2
      x2 = (x1p1 - x1p4)/2
    except:
      pass
    x3 = str(x1)
    x4 = str(x2)
    if ".0" in x3[1-2]:
      x1 = x3.split(".0")
      x1 = int(x1[0])
    if ".0" in x4[1-2]:
      x2 = x4.split(".0")
      x2 = int(x2[0])
    if str(type(x1)) == "<class 'complex'>":
      print("\nNo Solution (Negative Radical)")
      printed = True
    if x1 == x2:
      print("\nSolution:",x1)
    elif printed != True:
      print("\nSolution 1:",x1)
      print("Solution 2:",x2)
