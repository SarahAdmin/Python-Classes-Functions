class MyCar: 
  def __init__(self,brand,model,colour,numofseats,yearReleased) 
      self.brand = brand
      self.model = model 
      self.colour = colour 
      self.numofseats = numofseats 
      self.yearReleased = yearReleased 
  def CarFunction(self): 
      print('Brand:  '+ self.brand)
      print('Model:  '+ self.model) 
      print('Colour: '+ self.colour) 
      print('Number of Seats: '+ self.numofseats)
      print('Year: '+ self.yearReleased) 

Myparam = MyCar('Ford','Fiesta','White','Five','2024') 

Myparam.CarFunction()
