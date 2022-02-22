class help():
  def __init__(self):
    import os
    if os.name == "nt":
      os.system("cls")
    else:
      os.system("clear")
    print("Type equation.commands() to get started or click on 'Code' to read the README.md file for for information.")
