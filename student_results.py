import pandas as pd 
def CollegeResults(input_data,column_names): 
  df = pd.DataFrame(input_data,columns=column_names)
  return df 

myData = [['Lee Cox','Matt Bond','Lemon Jelly','Marcellina Adams','Jill Gates','Joe Malone'],
         ['FS','FS','FS','FS','FS','FS'], 
         ['L1','L1','E3','E3','L1','E3'],
         ['English','Maths','English','Maths','English','Maths'],
         [70,100,65,30,40,80]]
cols = ['Name','Qualification','Level','Subject','Percentage']
final_data = CollegeResults(myData,cols)
print(final_data)
