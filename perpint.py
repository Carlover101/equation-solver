class perpint:
    def __init__(self,eq,intsec):
        """
        'perpint' takes the slope of a known line and the coordinates of a known intersection point and finds the perpendicular line that intersects the known line at the intersection point.

        'eq' is the equation of the known line.
          - Form: y = mx + b
        
        'intsec' is the coordinate point of the known intersection point of the known line and the unknown perpendicular line.
          - Form: (x,y)
        """
        
        import re

        
        eq = self.eq
        intsec = self.intsec
        opp = re.sub("[^0-9/.-]","",eq)
        opp = opp.split("/")
        opp[0],opp[1] = int(opp[0]),int(opp[1])
        opp2 = -1*(opp[1]) / opp[0]
        
        if opp2 == 1.0:
            slope = 1
            calc = 0
            
        elif opp2 == -1.0:
            slope = -1
            calc = 0
            
        else:
            slope = opp2
            calc = 1
            
        if calc == -1:
            yint = 0
            
        elif calc == 0:
            if float(opp[0]) != 0:
                if "-" in opp[0]:
                    count = -1*opp[0]
                    
                else:
                    count = opp[0]
                    
                for i in range(count):
                    yint -= float(opp[0])
                    
        elif calc == 1:
            number = float(opp[1])
            number2 = 0.01
            number3 = slope
            number4 = float(opp[0])
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
        run = opp[0]
        rise = opp2
        if calc == -1:
            print(f"y = {opp[1]}")
            
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
                if run != 1:
                    print(f"y = {rise}/{run}x + {yint}")
                    
                elif run == 1:
                    print(f"y = {rise}x + {yint}")
                    
            elif yint < 0:
                print(f"y = {rise}/{run}x {yint}")
                