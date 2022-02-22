class commands():
  def __init__(self):
    import os
    if os.name == "nt":
      os.system("cls")
    else:
      os.system("clear")
    print("The commands are: \nequation.quadsolve() - For quadratic equations. \nequation.slopeint() - For slope-intercept equations. - NEW: May still have bugs, but works for right now :) \nequation.help() - Brings up the help page.")
