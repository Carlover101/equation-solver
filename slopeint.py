class slopeint():
    def __init__(self,x1,y1,x2,y2):
        """
        'slopeint' takes the x and y coordinates of two points and returns the slope-intercept equation of the line that crosses over the two points.

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
            
        yint = ""
        point1 = self.x1
        point2 = self.y1
        point3 = self.x2
        point4 = self.y2
        rise = float(point4) - float(point2)
        run = float(point3) - float(point1)
        
        if rise/run == 1.0:
            slope = 1
            calc = 0
            
        elif rise/run == -1.0:
            slope = -1
            calc = 0
            
        elif rise == 0:
            slope = "x"
            calc = -1
            
        else:
            slope = rise/run
            calc = 1
            
        if calc == -1:
            yint = 0
            
        elif calc == 0:
            if float(point1) != 0:
                yint -= float(point1)
                
        elif calc == 1:
            number = float(point4)
            number2 = 0.01
            number3 = slope
            number4 = float(point3)
            divider = 0
            status = None
            if number > 0:
                if number4 < 0:
                    while True:
                        if (number-number2)/number4 == number3:
                            break
                            
                        elif (number-number2)/number4 < number3:
                            if status != "smaller":
                                status = "smaller"
                                divider += 1
                                
                            number2 = number2 + (1 / (divider*10))
                            number2 = round(number2,divider+1)
                            
                        elif (number-number2)/number4 > number3:
                            if status != "larger":
                                status = "larger"
                                divider += 1
                                
                            number2 = number2 - (1 / (divider*10))
                            number2 = round(number2,divider+1)
                            
                elif number4 > 0:
                    while True:
                        if (number-number2)/number4 == number3:
                            break
                            
                        elif (number-number2)/number4 < number3:
                            if status != "smaller":
                                status = "smaller"
                                divider += 1
                                
                            number2 = number2 - (1 / (divider*10))
                            number2 = round(number2,divider+1)
                            
                        elif (number-number2)/number4 > number3:
                            if status != "larger":
                                status = "larger"
                                divider += 1
                                
                            number2 = number2 + (1 / (divider*10))
                            number2 = round(number2,divider+1)
                            
            elif number < 0:
                if number4 > 0:
                    while True:
                        if (number-number2)/number4 == number3:
                            break
                            
                        elif (number-number2)/number4 < number3:
                            if status != "smaller":
                                status = "smaller"
                                divider += 1
                                
                            number2 = number2 + (1 / (divider*10))
                            number2 = round(number2,divider+1)
                            
                        elif (number-number2)/number4 > number3:
                            if status != "larger":
                                status = "larger"
                                divider += 1
                                
                            number2 = number2 - (1 / (divider*10))
                            number2 = round(number2,divider+1)
                            
                elif number4 > 0:
                    while True:
                        if (number-number2)/number4 == number3:
                            break
                            
                        elif (number-number2)/number4 < number3:
                            if status != "smaller":
                                status = "smaller"
                                divider += 1
                                
                            number2 = number2 - (1 / (divider*10))
                            number2 = round(number2,divider+1)
                            
                        elif (number-number2)/number4 > number3:
                            if status != "larger":
                                status = "larger"
                                divider += 1
                                
                            number2 = number2 + (1 / (divider*10))
                            number2 = round(number2,divider+1)
                        
            yint = round(number2,1)
        if calc == -1:
            print(f"y = {point4}")
            
        elif yint == 0:
            if calc == 0:
                print(f"y = {slope}x")
                
            elif run == -1.0:
                print(f"y = {-1*rise}x")
                
            else:
                if rise % run == 0:
                    print(f"y = {rise/run}/{run/run}x")
                    
                elif run % rise == run / 0.5:
                    print(f"y = {rise/rise}/{run/rise}")
                    
                else:
                    print(f"y = {rise}/{run}")
                    
        elif calc == 0:
            if yint > 0:
                print(f"y = {slope}x + {yint}")
                
            elif yint < 0:
                print(f"y = {slope}x {yint}")
                
        elif run == -1.0:
            if yint > 0:
                print(f"y = {-1*rise}x + {yint}")
                
            elif yint < 0:
                print(f"y = {-1*rise}x {yint}")
                
        else:
            if yint > 0:
                print(f"y = {rise}/{run}x + {yint}")
                
            elif yint < 0:
                print(f"y = {rise}/{run}x {yint}")