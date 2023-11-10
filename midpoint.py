class midpoint():
    def __init__(self,x1,y1,x2,y2):
        """
        'midpoint' takes the x and y coordinates of two points and returns the midpoint (the point directly in between the two points).

        'x1' is the x coordinate of the first point.
        'y1' is the y coordinate of the first point.
        'x2' is the x coordinate of the second point.
        'y2' is the y coordinate of the second point.
        """
        
        import os

        
        if os.name == "nt":
            os.system("cls")
            
        else:
            os.system("clear")

        x1 = float(self.x1)
        x2 = float(self.x2)
        y1 = float(self.y1)
        y2 = float(self.y2)
        
        print(f"Midpoint: ({(x1 + x2)/2},{(y1 + y2)/2})")