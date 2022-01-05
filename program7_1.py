# Cole Class 2019

import random 

def main(): # Create main function 
    temperature = [] # Create an empty list 
    for i in range(0,25): # For and range fucntion to fill list 
        temperature.append(random.randint(5,75)) # Add numbers to list 
    for i in temperature:
        print(i , end=' ')
    print() # Print temperatures 
    highest = max(temperature) # Max temperature
    lowest = min(temperature) # Lowest temperature
    print('Highest temperature is ', highest,' and the lowest is ', lowest) # Print high and low
    if 32 in temperature:
        index = temperature.index(32) # Find if 32 is in the list
        print('Found 32F at index ', index)
    else:
        print('32F is not in the list')
    print('First 10 in the list ', temperature[:10]) # Print first 10
    print('Middle 5 in the list ', temperature[10:15]) # Print middle 5
    print('Final 10 in the list ', temperature[15:25]) # Print last 10
    freez_temperatures = custom_function(temperature) # Import custom function
    print('Found ', len(freez_temperatures), ' below freezing temperatures') # Print number of freezing temperatures
    freez_temperatures.sort # Sort list 
    print('Here are the below freezing temperatures...')
    for i in freez_temperatures: # print the freezing temperatures
        print(i, end=' ')
        
def custom_function(freez): # Custom function for freezing temperatures
    list2 = [] # Empty list 
    for i in freez: # Freeze is less than 32 
        if i < 32: 
            list2.append(i) # Add this to the empty list 
    return list2 # Return list2 to main function
          
main()
# This is origonal work from Cole Chervitz, I did not refrence any outside resources 
