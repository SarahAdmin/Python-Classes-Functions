def PowBy2(num): 
    findAPower = pow(num,2)
    return findAPower 
def PowBy3(num): 
    findAThree = pow(num,3)
    return findAThree

if __name__ == "__main__": 
    user_input = int(input("Enter a number: "))
    output_1 = PowBy2(user_input)
    output_2 = PowBy3(user_input)
    print(f'Power by 2: {output_1}')
    print(f'Power by 3: {output_2}')
