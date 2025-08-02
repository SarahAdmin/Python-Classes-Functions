def EvenNumber(num):
  thisIsEven = num % 2 == 0 
  return thisIsEven 

if __name__ == "__main__": 
  user_input = int(input('Enter a number: '))
  num_output = EvenNumber(user_input) 
print(num_output)
