import pandas as pd 
def PizzaOrder(input_data,column_names): 
  df = pd.DataFrame(input_data,columns=column_names)
  return df 

data = [['Lee Cox','Meat Feast',10,7.50],['Matt Bond','Pepperoni',8,5.00],['Joe Malone','Meat Feast',8,5.00],
        ['Jenny Banks','BBQ Chicken',10,7.50],['Marcelinna Adams','Pepperoni',8,5.00],['Paige Quinn','Cheese and Tomato',8,5.00],
        ['John Baxter','Meat Feast',10,7.50],['Gill Gates','Pepperoni',10,7.50]]
cols = ['Name','Topping','Size','Price']
final_data = PizzaOrder(data,cols) 
print(final_data)
                                                                                       
