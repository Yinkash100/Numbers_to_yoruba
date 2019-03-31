#num2yoruba: is a dictionary that points each number in the unit position to words in yoruba
num2yoruba = { 1:'ookan', 2:'eeji', 3:'eeta', 4:'eerin', 5:'aarun', 6:'eefa', 7:'eeje', 8:'eejo', 9:'eesan', 10:'eewa',
               11:'okanla', 12:'eejila', 13:'eetala', 14:'eerinla'}

#num2yoruba_tens: a dictionary that points each number in the tenth to words in yoruba
num2yoruba_tens = { 2:'ogoji', 3:'ogbon', 4:'ogoji', 5:'aadota', 6:'oogota', 7:'aadorin', 8:'ogorin', 9:'aadorin', 10:'ogorun',
               11:'aadofa', 12:'ogofa', 13:'aadoje', 14:'ogoje', 15:'aadojo', 16:'ogojo', 17:'aadosan', 18:'ogosan', 19:'aadowa', 20:'igba',
                    }

def convert_tens(number):
    """
        convert the number in the tenth position to yoruba word
        
    """
    tens, unit = divmod(number, 10)
    if unit < 5:
            if unit == 0:
            word_equivalent = num2yoruba_tens[tens]
        else:
            word_equivalent = num2yoruba[unit] + 'lel' + num2yoruba_tens[tens]
        return word_equivalent

    else:
        tens += 1
        unit = 10 - unit
        word_equivalent = num2yoruba[unit]+'dinl'+ num2yoruba_tens[tens]
        return word_equivalent

def convert_number(number):
    """
        converts the input to words in yoruba
    """
    if number >= 0 and number <= 14:
        return num2yoruba[number]
    elif number >=15 <= 200:
        return convert_tens(number)
    else:
        return 'Sorry, this program cannot convert the number'

def main():
    #creates 200 random numbers and convert it to words in  yoruba
    i = 200
    while i > 0:
        num = random.randint(1, 200)
        print(num)
        print(num, convert_number(num))
        i=i-1

import random
main()
