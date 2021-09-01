# This is a program in Python to convert a user input temperature from the Farenheit scale to the Celsius scale

input_temp = float(input("Enter the temperature in Farenheit: "))
celsius_temp = (input_temp-32)*5/9
print("The temperature in degrees celsius is ", celsius_temp)