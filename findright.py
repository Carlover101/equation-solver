class findright():
    def __init__(self,missing,s1,s2):
        """
        'findright' finds the missing side of a right triangle from two known sides.

        'missing' tells the program whether the missing side is the hyptenuse or a leg.
          - Type 'hypotenuse' or 'h' if the missing side is the hypotenuse.
          - Type 'leg' or 'l' if the missing side is a leg.

        's1' is the length of the first known side.
        's2' is the length of the second known side.
        """
        
        import math
        import os

        
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

        leghyp = self.missing.lower()
        length1 = int(self.s1)
        length2 = int(self.s2)
    
        if leghyp == "hypotenuse" or leghyp == "h":
            return math.sqrt((int(length1)**2 + int(length2)**2))
    
        elif leghyp == "leg" or leghyp == "l":
            try:
                return math.sqrt(int(length1)**2 - int(length2)**2)

            except:
                return math.sqrt(int(length2)**2 - int(length1)**2)