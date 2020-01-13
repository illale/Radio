HEX = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "a": 10,
        "b": 11,
        "c": 12,
        "d": 13,
        "e": 14,
        "f": 15 }
        
DECIMAL = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f" }
        
HEX_BIT = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "a": "1010",
        "b": "1011",
        "c": "1100",
        "d": "1101",
        "e": "1110",
        "f": "1111" }
        
BIT_HEX = {
        "0": "0",
        "1": "1",
        "10": "2",
        "11": "3",
        "100": "4",
        "101": "5",
        "110": "6",
        "111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "a",
        "1011": "b",
        "1100": "c",
        "1101": "d",
        "1110": "e",
        "1111": "f" }
 
def hex_to_decimal(hex):
    """
    Hexadecimal is base 16 number represented by charachter "0123456789abcdef"
    22e is an hexadecimal number. It can be converted to decimal number by:
    multiply each character with exponent of 16. For example 22e is converted like this.
    2 * 16 ^ 2 + 2 * 16 ^ 1 + 14 * 16 ^ 0, (e = 14). Outcome of this hexadecimal is 
    decimal number 558. This converter expects hexadecimal to be in string format.
    """
    result = 0
    for i, number in enumerate(hex):
        multiplier = len(hex) - (i + 1)
        result += HEX[number] * 16 ** multiplier   
    return result

def binary_to_decimal(binary):
    """ 
    Binary number is base 2 number represented by 1's and 0's.
    For example 10011 is binary number. Binary numbers can be converted
    to decimal number by calculating the sum of all 1's and 0's when they are
    multiplied by 2 ^ x, (x is the number, which points the position of the
    particular bit) For example 10011 is converted like this: 1 * 2^4 + 0 * 2^3 + 
    0 * 2^2 + 1 * 2^1 + 1 * 2^0. The result is decimal number 19
    """
    result = 0
    for i, number in enumerate(binary):
        multiplier = len(binary) - (i + 1)
        result += int(number) * (2 ** multiplier)  
    return result

def decimal_to_hex(number):
    """
    Converts base 10 decimal number to base 16 hexadecimal number.
    """
    division = number // 16
    remainder = number % 16
    result = ""
    while True:
        if remainder > 9:
            key = "{}".format(remainder)
            result += DECIMAL[key]
        else:
            result += "{}".format(remainder)
        
        remainder = division % 16
        division = division // 16
        if division == 0:
            if remainder > 9:
                key = "{}".format(remainder)
                result += DECIMAL[key]
            else:
                result += "{}".format(remainder)
            result = result[::-1]
            return result
        
def decimal_to_binary(number):
    """
    Decimal numbers can be converted to binary numbers. This happens by turning the 
    number into sums of exponets of two. For example 13 = 1 * 2 ^ 3 + 1 * 2 ^ 2 + 0 * 2 ^ 1 + 1 * 2 ^ 0.
    The exponents have multiplier of 1 or 0. Then we take the multiplies and the result
    is binary number 13 = 1101.
    """
    start = number
    i = 0
    while True:
        if 2 ** (i + 1) > number:
            break
        else:
            i += 1
            
    result = ""
    while True:
        r = 2 ** i
        if r > number:
            result += "0"
        else:
            result += "1"
            number = number - r
        i -= 1
        if r == 1:
            return result
        
def hex_to_binary(hex):
    result = ""
    for num in hex:
        result += HEX_BIT[num]
        
    return result
def binary_to_hex(binary):
    result = ""
    for i in range(len(binary) // 4):
       sli = binary[4 * i: 4 * (i + 1)]
       key = "{}".format(int(sli))
       result += BIT_HEX[key]
       
    return result
       

if __name__ == "__main__":
    """print("Examples:")
    print("fa32d =", hex_to_decimal("fa32d"))
    print("110101001 =", binary_to_decimal("110101001"))
    print("255 =", decimal_to_hex(255))
    print("65535 =", decimal_to_binary(65535))
    print("5da3 in binary =", hex_to_binary("5da3"))
    print("10110110 in hex =", binary_to_hex("10110110"))"""
    print(hex_to_binary("21"))
    print(hex_to_binary("4e"))
    print(hex_to_binary("63"))
    print(hex_to_binary("31"))
    print(hex_to_binary("39"))
    print(hex_to_binary("63"))
    print(hex_to_binary("6e"))
    print(hex_to_binary("39"))
    print(hex_to_binary("39"))
    print(hex_to_binary("3f"))
    print(hex_to_binary("2d"))
    