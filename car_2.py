class Car: 
    def __init__(self,make,model,colour,year):
        self.make = make
        self.model = model 
        self.colour = colour 
        self.year = year
    
    def myCar(self): 
        print(f'Make: {self.make}')
        print(f'Model: {self.model}')
        print(f'Colour: {self.colour}')
        print(f'Year: {self.year}')

carOne = Car('Toyota','Yaris','Black','2024')

carOne.myCar()
