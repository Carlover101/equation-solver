class quadsolve():
    def __init__(self,eq):
        """
        'quadsolve' takes a quadratic equation and returns it's solution(s) (if any), as well as the a, b, and c of the equation.

        'eq' is the quadratic equation.
          - Form: ax^2 + bx + c
        """
        
        import re
        import os

        
        if os.name == "nt":
            os.system("cls")
            
        else:
            os.system("clear")
            
        printed = ""
        quadratic = self.eq
        nospaces = re.sub("[^0-9-.*/()+x^=]", "", quadratic)
        if "=0" in nospaces:
            nospaces = nospaces.split("=0")
            nospaces = nospaces[0]
            
        if "x**2" in nospaces:
            a = nospaces.split("x**2")
            
        elif "x^2" in nospaces:
            a = nospaces.split("x^2")
            
        if a[0] == "":
            a[0] = "1"
            
        if "x" not in a[1]:
            b = 0
            c = re.sub("[^0-9-.*()/]", "", a[1])
            a = a[0]
            
        else:
            c = a[1].split("x")
            b = re.sub("[^0-9-.*()/]", "", c[0])
            if b == "":
                b = "1"
                
            elif b == "-":
                b = "-1"
                
            a = re.sub("[^0-9-.*()/]", "", a[0])
            c = re.sub("[^0-9-.*()/]", "", c[1])
            
        if "--" in c:
            c = re.sub("[^0-9.*()/]", "", c)
            
        try:
            a = float(a)
            
        except:
            if "/" in a:
                a = a.split("/")
                a = float(int(a[0]) / int(a[1]))
                
        try:
            b = float(b)
            
        except:
            if "/" in b:
                b = b.split("/")
                b = float(int(b[0]) / int(b[1]))
                
        try:
            c = float(c)
            
        except:
            if "/" in c:
                c = c.split("/")
                c = float(int(c[0]) / int(c[1]))
                
        try:
            x1p1 = -b
            x1p2 = b**2
            x1p3 = -4*(a*c)
            x1p4 = (x1p2 + x1p3)**0.5
            x1 = (x1p1 + x1p4)/(2*a)
            x2 = (x1p1 - x1p4)/(2*a)
            
        except:
            pass
            
        if str(type(x1)) == "<class 'complex'>":
            print("\nNo Solution (Negative Radical)")
            printed = True
            
        if x1 == x2:
            print("\nSolution:",x1)
            
        elif printed != True:
            print("\nSolution 1:",x1)
            print("Solution 2:",x2)