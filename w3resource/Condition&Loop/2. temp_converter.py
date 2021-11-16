#[Formula: c/5 = f-32/9 [where c = temperature in celsius and f = temperature in fahrenheit]
 #Expected Output:
 #60°C is 140 in Fahrenheit
 #45°F is 7 in Celsius

#1. Possible Method, but very easy
# tempC = int(input('Enter temperature in Celsius :'))
# tempF = int(input('enter temperature in Farenheit :'))
# tempC = 60
# tempF = 45

# tempCF = int(((tempC/5)*9)+32)
# tempFC = int(((tempF-32)/9)*5)

# print(str(tempC) + '°C is ' + str(tempCF) + ' in Farenheit')
# print(str(tempF) + '°F is ' + str(tempFC) + ' in Celsius')


#2. Smarter method
temp = input('Enter Temperature with degree like 45C or 56F: ')
degree = int(temp[:-1])
convention = temp[-1]
if convention.upper() == 'C':
    result = int(round((9*degree)/5+32))
    convention = 'Farenheit'
elif convention.upper() == 'F':
    result = int(5*(degree-32)/9)
    convention = 'Celsius'
else:
    print('Convention was not right, please try again')
print('Temperature in ', convention, 'is', result, 'degrees')