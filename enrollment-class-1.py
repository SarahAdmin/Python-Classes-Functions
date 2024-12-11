class Student: 
  def __init__(self,name,course,level): 
    self.name = name
    self.course = course
    self.level = level 
    
  def EnrolStudent(self): 
    print('Name: '+ self.name)
    print('Course: '+ self.course)
    print('Level: '+ self.level)

paramOne = Student('Lemon Jelly','ICT','2') 
paramOne.EnrolStudent() 

paramTwo = Student('Matt Bond','Media','3')
paramTwo.EnrolStudent() 


  
