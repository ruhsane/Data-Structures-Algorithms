#!python

import string
import math
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
    # TODO: Decode digits from binary (base 2)
    if base == 2 :
        result = 0
        nth = -1
        for value in reversed(digits):
            nth += 1
            if value == "1" :
                print(nth)
                result += math.pow(2, nth)
        return int(result)
    
    # TODO: Decode digits from hexadecimal (base 16)
    elif base == 16:
        sum = 0
        power = len(digits)
        for value in digits:
            print(value)
            power -= 1
            sum += string.hexdigits.index(value.lower()) * math.pow(16, power)
        return int(sum)

    # TODO: Decode digits from any base (2 up to 36)
    else:
        sum = 0
        power = len(digits)
        for value in digits:
            print(value)
            power -= 1
            sum += string.printable.index(value.lower()) * math.pow(base, power)
        return int(sum)


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
            return number

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
            return number

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
            return number

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
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    
    finalResult = ''

    # exclude spaces from the inputted binary digit
    digits = digits.replace(" ", "")

    # make sure the input is sectioned by 4
    zeroNeededinfront = 4- (len(digits) % 4)
    if zeroNeededinfront != 4 :
        digits = '0' * zeroNeededinfront + digits
    
    # we are gonna loop through the sections of the input (each includes 4 numbers) and convert each section to hex
    # start at index 3, grab four numbers before current index including current index, until the end of the digits
    for i in range(3, len(digits), 4):
        section = digits[i-3:i+1]
        # decode this section binaryToDecimal/hexToDecimal
        decimal = decode(section, base1)
        # encode this section's decimal into hex/binary
        resultOfSection = str(encode(decimal, base2))

        finalResult += resultOfSection

    return finalResult

    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        # result = convert(digits, base1, base2)
        # print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    # main()
    # print(decode('123', 10))
    print(encode(237, 36))
    print(encode(1, 36))
    print(encode(0, 36))
    print(encode(15, 36))
    print(encode(54, 36))
    print(encode(255, 36))