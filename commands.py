class commands():
  def __init__(self):
    """
    'commands()' simply gives a list of available functions and a brief sumary of what they do.

    For more help, type 'help(function)' - replace 'function' with the name of the function.
    """
      
    import os

      
    if os.name == "nt":
      os.system("cls")
        
    else:
      os.system("clear")
        
    print("The commands are: \neqsolve.quadsolve() - For quadratic equations. \neqsolve.slopeint() - For slope-intercept equations. \neqsolve.midpoint() - For finding the midpoint of two points. \neqsolve.perpint() - Takes a slope and an intersection point and returns the slope-intercept equation of the perpendicular line. \neqsolve.issim() - Takes the lengths of the sides of one shape and the corresponding sides of a second shape and calculates if they are similar. \neqsolve.findright() - Finds the missing length of a right triangle. \neqsolve.help() - Brings up the help page. \neqsolve.intcompound() - Calculates compounded interest. \neqsolve.contcompound() - Calculates continuously compounded interest.\n\nFor more help, type 'help(function)' - replace 'function' with the name of the function.")