class issim:
  def __init__(self):
    import os
    if os.name == "nt":
      os.system("cls")
    else:
      os.system("clear")
    shape1 = input(f"Input the side lengths of the first shape in order separated by commas: ")
    shape2 = input(f"Input the corresponding side lengths of the second shape separated by commas: ")
    shape1 = shape1.split(",")
    shape2 = shape2.split(",")
    if len(shape1) != len(shape2):
      print("This function is for testing if two shapes with completely declared side lengths are similar. Please use equation.findsim() to try to find mising side lengths.")
    else:
      sim = ""
      scales = []
      for i in range(len(shape1)):
        scales.append(int(shape2[i])/int(shape1[i]))
      for i in range(len(scales)):
        if i != 0:
          if scales[i] != scales[i-1]:
            print("The shapes are not similar.")
            sim = False
            break
      if sim != False:
        print(f"The shapes are similar and the scale factor is {scales[0]}.")
