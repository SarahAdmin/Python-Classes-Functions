def ReverseLetter(str):
    backwards_text = str[::-1]
    return backwards_text 

if __name__ == "__main__": 
    user_input = input('Enter a word: ')
    text_output = ReverseLetter(user_input)
    print(f'The backward text is {text_output}')
