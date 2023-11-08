#Task 1: Using Old Style Formatting

'''
75 Fahrenheit = 23.888900 Celsius
75 Fahrenheit = 23.89 Celsius
75 Fahrenheit = 000023.889 Celsius
75 Fahrenheit = 23.889 	Celsius
75 Fahrenheit = 	23.889 Celsius
75 Fahrenheit = 2.389E+01 Celsius
75 Fahrenheit = 2.389e+01 Celsius
'''
F = 75
C = 23.8889

print('%d Fahrenheit = %f Celsius' % (F, C))
print('%d Fahrenheit = %.2f Celsius' % (F, C))
print('%d Fahrenheit = %06.3f Celsius' % (F, C))
print('%d Fahrenheit = %6.3f Celsius' % (F, C))
print('%d Fahrenheit = %6.3f Celsius' % (F, C))
print('%d Fahrenheit = %6.3E Celsius' % (F, C))
print('%d Fahrenheit = %6.3e Celsius' % (F, C))


 

first_name = 'Tamara'
last_name = 'Babic'
'''
Name: Tamara Babic
Name: Tamara      	Babic
Name: Tamara		Babic
Name: 	Tamara		Babic
Name: 	Tamara Babic
Name: 	Tamara Babic 	
'''

print('Name: %s %s' % (first_name, last_name))
print('Name: %s %10s' % (first_name, last_name))
print('Name: %s %10s' % (first_name, last_name))
print('Name: %10s %10s' % (first_name, last_name))
print('Name: %10s %s' % (first_name, last_name))
print('Name: %10s %s %10s' % (first_name, last_name, last_name))


#Task 2: Using Python-Style Formatting(new way)

#Use Python-style formatting and the variables `F` and `C` to generate the following print outputs

'''
75 Fahrenheit = 23.888900 Celsius
75 Fahrenheit = 23.89 Celsius
75 Fahrenheit = 0000023.89 Celsius
75 Fahrenheit = 23.889 	Celsius
75 Fahrenheit =   23.889   Celsius
75 Fahrenheit = 	23.889 Celsius
75 Fahrenheit = 2.389E+01 Celsius
'''
 
F = 75
C = 23.8889

print('{} Fahrenheit = {} Celsius'.format(F, C))
print('{0} Fahrenheit = {1:.2f} Celsius'.format(F, C))
print('{0} Fahrenheit = {1:06.2f} Celsius'.format(F, C))
print('{0} Fahrenheit = {1:6.3f} Celsius'.format(F, C))
print('{0} Fahrenheit = {1:6.3f} Celsius'.format(F, C))
print('{0} Fahrenheit = {1:6.3E} Celsius'.format(F, C))
print('{0} Fahrenheit = {1:6.3e} Celsius'.format(F, C))


 

first_name = 'Tamara'
last_name = 'Babic'

'''
Name: Tamara Babic
Name: Tamara      	Babic
Name: Tamara		Babic
Name: 	Tamara		Babic
Name: 	Tamara Babic
Name: 	Tamara Babic 	
'''

print('Name: {0} {1}'.format(first_name, last_name))
print('Name: {0} {1:10}'.format(first_name, last_name))
print('Name: {0} {1:10}'.format(first_name, last_name))
print('Name: {0:10} {1:10}'.format(first_name, last_name))
print('Name: {0:10} {1}'.format(first_name, last_name))
print('Name: {0:10} {1} {1:10}'.format(first_name, last_name))
