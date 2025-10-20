import pandas as pd 
def MyEmployers(input_data,column_names): 
  df = pd.DataFrame(input_data,columns=column_names)
  return df 

data = [['Lee Cox','Computer Scientist','Dell',35000],['Matt Bond','Financial Analyst','Natwest',40000],['Gill Gates','Computer Scientist','Microsoft',80000], 
        ['Pamela Adams','Lawyer','Dentons',50000],['John Baxter','Financial Analyst','Nationwide',45000],['Lemon Jelly','Ecomonist','Visa',40000],['Jonah Parker','Journalist','BBC',35000],
        ['Emma Green','Project Manager','SAP',80000]] 
cols = ['Name','Position','Company','Salary']  
final_data = MyEmployers(data,cols) 
print(final_data)
