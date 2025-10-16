import pandas as pd
def myCars(input_data,column_names): 
  df = pd.DataFrame(input_data,columns=column_names)
  return df 
data = [["Toyota","Ford","Volkswagen"],["Yaris,","Fiesta","T-Cross"],:["Red","Blue","Black"],:[5,5,5],[2019,2024,2020]]
cols = ['Make','Model','Colour','No_of_Seats','Year']
final_data = myCars(data,cols)
print(final_data)
