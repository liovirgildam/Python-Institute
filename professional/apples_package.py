import random 

class Package:
    apples = 0
    weight = 0
    
    
class Apple(Package):
   
    def __init__(self):
        super().__init__
        Package.apples += 1
        Package.weight += random.uniform(0.2, 0.5)
        
     
while Package.apples < 1000 and Package.weight <= 299.5 :
    apple = Apple()

print(f"Total apples: {Package.apples} and total weight: {Package.weight}")
        
         