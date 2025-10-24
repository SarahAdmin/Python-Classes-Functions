import pandas as pd
def MyCars(input_data,column_names):
    df = pd.DataFrame(input_data,columns=column_names)
    return df 

data = [['Toyota','Yaris','Red',2025],['Ford','Fiesta','Blue',2024],['Volkswagen','T-Cross','Black',2024],['Toyota','Yaris','Grey',2024],['Fiat','500e','White',2024],['Ford','Fiesta','White',2023],['Toyota','Yaris','Grey',2020],['Fiat','600e','Navy Blue',2025]]
cols = ['Make','Model','Colour','Year']
final_data = MyCars(data,cols)
print(final_data)
