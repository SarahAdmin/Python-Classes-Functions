import pandas as pd 
def CollegeResults(input_data,column_names): 
  df = pd.DataFrame(input_data,columns=column_names)
  return df 

myData = [['Lee Cox','FS','L1','English',70],['Matt Bond','FS','L1','Maths',100],['Lemon Jelly','FS','E3','English',65],['Marcellina Adams','FS''E3','Maths',30],
 ['Jill Gates','FS','L1','English',40],['Joe Malone','FS','E3','Maths',80]]
cols = ['Name','Qualification','Level','Subject','Percentage']
final_data = CollegeResults(myData,cols)
print(final_data)


