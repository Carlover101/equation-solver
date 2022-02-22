class commands():
  def __init__(self):
    import os
    if os.name == "nt":
      os.system("cls")
    else:
      os.system("clear")
    print("The commands are: \neqsolvcarlover101.quadsolve() - For quadratic equations. \neqsolvcarlover101.slopeint() - For slope-intercept equations. \neqsolvcarlover101.midpoint() - For finding the midpoint of two points. \neqsolvcarlover101.help() - Brings up the help page.")
