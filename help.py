class help():
    def __init__(self):
        """
        'help()' tells you how to find the names of functions or where to find extended help.
        """
        
        import os

        
        if os.name == "nt":
            os.system("cls")
            
        else:
            os.system("clear")
            
        print("Type eqsolve.commands() to get started or read the README.md file for more information.")