class intcompound:
    def __init__(self,p,r,n,t):
        """
        This function gives you the amount of money that will be present or owed after a number of years.

        'p' is the principal (Initial) amount.
        'r' is the interest rate.
        'n' is the number of times the interest is compounded (added to your total) yearly.
        't' is the amount of time passed in years.
        """
        
        p = float(self.p)
        r = float(self.r)/100
        n = float(self.n)
        t = float(self.t)

        return f"${round((p*((1+(r/n))**(n*t))),2)}"