class issim:
    def __init__(self,shape1,shape2):
        """
        'issim' determines whether two shapes are considered similar. If so, it returns the factor by which the shape was scaled.

        'shape1' is the lengths of the sides, separated by commas, of the first shape in an order.
        'shape2' is the lengths of the sides, separated by commas, of the seconds shape in the same order as the first.
        """
        
        import os

        
        if os.name == "nt":
            os.system("cls")
            
        else:
            os.system("clear")
            
        shape1 = self.shape1
        shape2 = self.shape2
        shape1 = shape1.split(",")
        shape2 = shape2.split(",")
        
        if len(shape1) != len(shape2):
            return "This function is for testing if two shapes with completely declared side lengths are similar."
            
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
                return f"The shapes are similar. The scale factor is {scales[0]}."