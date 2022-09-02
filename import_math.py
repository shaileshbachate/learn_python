# Built-in Math Functions #
print(f'abs(-7.34)      :   {abs(-7.34)}')
print(f'min(15,10,25)   :   {min(15,10,25)}')
print(f'max(15,10,25)   :   {max(15,10,25)}')
print(f'min([4,12,36])  :   {min([4,12,36])}')
print('max({4,12,36})  :  ', max({4,12,36}))
print(f'pow(4, 3)       :   {pow(4, 3)}')
print(f'pow(25, 2.5)    :   {pow(25, 2.5)}')

print("------------------------------------------------------------------------")

# Python has also a built-in module called math, which extends the list of mathematical functions. #
import math

print(math.sqrt(25))
print(math.sqrt(25.25))
print(math.pow(25, 2.5))
print(math.ceil(4.34))
print(math.floor(4.34))
print(math.trunc(4.34))
print("------------------------------------------------------------------------")

PI = math.pi
print(PI)
print(math.e)   # Euler's number (2.7182...)
print(math.tau)
print(math.inf) # a floating-point positive infinity
print(math.nan) # a floating-point NaN (Not a Number) value. This value is not a legal number. 
# # The nan constant is equivalent to float('nan').
# print(float('nan'))
print("------------------------------------------------------------------------")

# find the exponential of the specified value
# The math.exp() method returns E raised to the power of x (Ex)
print(math.exp(math.e), 'is same as', math.e**math.e)
print(math.exp(65))
print(math.exp(-6.89))
print("------------------------------------------------------------------------")

# Log
# Return the natural logarithm of different numbers
# Syntax # math.log(x, base) # base is Optional. The logarithmic base to use. Default is 'e'

print(math.log(math.e), math.log(2), math.log(1), math.log(10))
print("------------------------------------------------------------------------")

# Return the base-10 logarithm of different numbers
print(math.log(2.7183, 10), math.log(2, 10), math.log(1, 10), math.log(10, 10))

# Return the base-10 logarithm of different numbers
print(math.log10(2.7183), math.log10(2), math.log10(1), math.log10(10))
print("------------------------------------------------------------------------")
