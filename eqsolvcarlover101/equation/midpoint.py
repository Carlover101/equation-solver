class midpoint():
  def __init__(self):
    import re
    import os
    if os.name == "nt":
      os.system("cls")
    else:
      os.system("clear")
    points = input("Enter two points. ( ex. (-1,2),(1,-2) ): ")
    points = points.split(",")
    point1 = int(re.sub("[^0-9.-]","",points[0]))
    point2 = int(re.sub("[^0-9.-]","",points[1]))
    point3 = int(re.sub("[^0-9.-]","",points[2]))
    point4 = int(re.sub("[^0-9.-]","",points[3]))
    print(f"Midpoint: ({(point1 + point3)/2},{(point2 + point4)/2})")
