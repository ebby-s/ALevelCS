roman = MCMLXXXI
number = 1981

global r_to_num
global num_to_r
r_to_num = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
num_to_r = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}

def roman_to_num(roman):
    number = 0
    for i in range(len(roman)):
        if i < len(roman)-1:
            if r_to_num[roman[i]] < r_to_num[roman[i+1]]:
                number -= r_to_num[roman[i]]
            else:
                number += r_to_num[roman[i]]
        else:
            number += r_to_num[roman[i]]
    return number

def num_to_roman(number):
    roman = ""
    for val in reversed(sorted(num_to_r.keys())):
        while number >= val:
            number -= val
            roman += num_to_r[val]
    return roman


