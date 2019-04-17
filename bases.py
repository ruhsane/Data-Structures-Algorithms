#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    fractional = False
    result = 0
    power = len(digits)

    #handle fractional number
    if '.' in digits:
        # get the length of characters before the dicimal point. set it as the power. so later when we minus 1 from the power after the dot, it becomes negative
        power = len(digits.split('.')[0])

        if base != 10:
            #remove the decimal point since later we are gonna math.power each character in the string
            digits = digits.replace(".", "")

        #set fractional = true
        fractional = True

    if base == 10:
        if '.' in digits:
            result = float(digits)
        else:
            result = int(digits)
    
    # Decode digits from any base (2 up to 36)
    else:
        for value in digits:
            power -= 1
            result += string.printable.index(value.lower()) * (base ** power)

    if fractional == True :
        print(result)

        return result
    else:
        return int(result)


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    """
        Divide the number by 2.
        Get the remainder for the binary digit. (it is gonna be either 0 or 1) and write from right to left each iteration
        Get the integer quotient for the next iteration.
        Repeat the steps until the quotient is equal to 0.

        final remainder list is gonna be the value
    """
    if base == 2:
        returnValue = ''

        if number == 0:
            return '0'

        while number != 0 :
            remainder = number % 2
            returnValue = str(remainder) + returnValue 

            # get integer quotient for the next iteration
            number = number // 2

        return returnValue

    # TODO: Encode number in hexadecimal (base 16)
    # ...
    '''
        Divide the number by 16.
        Get the remainder for the hex digit. and write from right to left each iteration
        Get the integer quotient for the next iteration.
        Repeat the steps until the quotient is equal to 0.
    '''
    if base == 16:
        returnValue = ''

        if number == 0:
            return '0'

        while number != 0 :
            remainder = string.hexdigits[number % 16]
            returnValue = str(remainder) + returnValue 

            # get integer quotient for the next iteration
            number = number // 16

        return returnValue


    # TODO: Encode number in any base (2 up to 36)
    # ...
    else:
        returnValue = ''

        if number == 0:
            return '0'

        while number != 0 :
            remainder = string.printable[number % base]
            returnValue = str(remainder) + returnValue 

            # get integer quotient for the next iteration
            number = number // base

        return returnValue


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    
    # exclude spaces from the inputted binary digit
    digits = digits.replace(" ", "")

    # Convert digits from any base to any base (2 up to 36)
    base10 = decode(digits, base1)
    result = str(encode(base10, base2))
    return result

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()