class findright():
  def __init__(self):
    import math
    import os
    if os.name == "nt":
      os.system("cls")
    else:
      os.system("clear")

    leghyp = input("Which side length is missing? (leg/l or hypontenuse/h): ").lower()
    lengths = input("Enter the other two side lengths separated by commas: ")
    lengths = lengths.split(",")
    
    if leghyp == "hypotenuse" or leghyp == "h":
      print(math.sqrt((int(lengths[0])**2 + int(lengths[1])**2)))
    
    elif leghyp == "leg" or leghyp == "l":
      try:
        print(math.sqrt(int(lengths[0])**2 - int(lengths[1])**2))

      except:
        print(math.sqrt(int(lengths[1])**2 - int(lengths[0])**2))
