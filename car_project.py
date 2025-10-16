import pandas as pd
def myCars(input_data,column_names): 
  df = pd.DataFrame(input_data,columns=column_names)
  return df 
data = [["Toyota","Yaris","Red",5,2019],["Ford","Fiesta","Blue",5,2024],["Volkswagen","T-Cross","Black",5,2020]]
cols = ['Make','Model','Colour','No_of_Seats','Year']
final_data = myCars(data,cols)
print(final_data)
