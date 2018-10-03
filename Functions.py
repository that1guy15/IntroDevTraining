# Repeatable code

x = 5
y = x **2

print(y)

x = 2
y = x **2

print(y)

y3 = x**3

print(y2)


def square(number):
    y = number**2
    return y

square(2)

def exponent(number, exponent):
    y = number**exponent
    return y

exponent(5, 2)

# Var y lives inside function no globally
print(y)

# Functions can call other functions
def exponent(number, exponent):
    if exponent == 2:
        y = square(number)
        print('square {}:'.format(number))
    else:
        y = number**exponent
        print('raise {} to the power of {}:'.format(number, exponent))
    return y