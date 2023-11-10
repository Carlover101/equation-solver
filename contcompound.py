class contcompound:
    def __init__(self,p,r,t):
        """
        'contcompound()' gives you the amount of money present or owed with a continuously compounding interest over a numbers of years.

        'p' is the principal (initial) amount.
        'r' is the interest rate.
        't' is the amount of time passed (in years).
        """
        
        p = float(self.p)
        r = float(self.r)/100
        t = float(self.t)
        e = 2.718281828459045

        return f"${round((p*(e**(r*t))),2)}"
        