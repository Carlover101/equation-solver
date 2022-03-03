class commands():
  def __init__(self):
    import os
    if os.name == "nt":
      os.system("cls")
    else:
      os.system("clear")
    print("The commands are: \neqsolvcarlover101.quadsolve() - For quadratic equations. \neqsolvcarlover101.slopeint() - For slope-intercept equations. \neqsolvcarlover101.midpoint() - For finding the midpoint of two points. \neqsolvcarlover101.perpint() - Takes a slope and an intersection point and returns the slope-intercept equation of the perpendicular line. \neqsolvcarlover101.issim() - Takes the lengths of the sides of one shape and the corresponding sides of a second shape and calculates if they are similar. \neqsolvcarlover101.help() - Brings up the help page.")
