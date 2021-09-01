terminate_keywords = ['stop','end','cancel','quit','terminate']

input_string = 'start'
while True:

    input_string = str(input("Enter a string to be printed: "))

    if input_string in terminate_keywords:
        
        break
    
    print(input_string)