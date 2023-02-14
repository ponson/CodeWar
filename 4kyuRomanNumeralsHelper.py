class RomanNumerals:

    @staticmethod
    def to_roman(val):
        def digit_i_to_r(n, rstr_idx):
            ROMAN_BY_DIGITS = [('I', 'V', 'X'), ('X', 'L', 'C'), ('C', 'D', 'M'), ('M', 'M', 'M')]
            rstr = ROMAN_BY_DIGITS[rstr_idx]

            def transfer_0_to_r(roman_list):
                return ''
            
            def transfer_1_to_r(roman_list):
                return roman_list[0]
            
            def transfer_2_to_r(roman_list):
                return roman_list[0]*2
            
            def transfer_3_to_r(roman_list):
                return roman_list[0]*3
            
            def transfer_4_to_r(roman_list):
                return ''.join([roman_list[0], roman_list[1]])
            
            def transfer_5_to_r(roman_list):
                return roman_list[1]
            
            def transfer_6_to_r(roman_list):
                return ''.join([roman_list[1], roman_list[0]])
            
            def transfer_7_to_r(roman_list):
                return ''.join([roman_list[1], roman_list[0], roman_list[0]])
            
            def transfer_8_to_r(roman_list):
                return ''.join([roman_list[1], roman_list[0], roman_list[0], roman_list[0]])
            
            def transfer_9_to_r(roman_list):
                return ''.join([roman_list[0], roman_list[2]])
            
            transfer_func = [transfer_0_to_r, transfer_1_to_r, transfer_2_to_r, transfer_3_to_r, transfer_4_to_r, transfer_5_to_r, transfer_6_to_r, transfer_7_to_r, transfer_8_to_r, transfer_9_to_r]

            return transfer_func[n](rstr)
        val_str = str(val)
        max_digit = len(val_str) - 1
        result = ''
        for idx, digit in enumerate(val_str):
            result += digit_i_to_r(int(digit), max_digit-idx)
       
        return result

    @staticmethod
    def from_roman(roman_num):
        DIGITS_TO_ROMAN = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        length = len(roman_num)
        result = 0
        if length == 1:
            return DIGITS_TO_ROMAN[roman_num[0]]
        else:
            for idx, rdigit in enumerate(roman_num):
                if idx < length - 1 and DIGITS_TO_ROMAN[rdigit] < DIGITS_TO_ROMAN[roman_num[idx+1]]:
                    result -= DIGITS_TO_ROMAN[rdigit]
                else:
                    result += DIGITS_TO_ROMAN[rdigit]
                        
        return result


print(RomanNumerals.to_roman(1000))
print(RomanNumerals.to_roman(4))
print(RomanNumerals.to_roman(1))
print(RomanNumerals.to_roman(1990))
print(RomanNumerals.to_roman(2008))

print(RomanNumerals.from_roman('XXI'))
print(RomanNumerals.from_roman('I'))
print(RomanNumerals.from_roman('IV'))
print(RomanNumerals.from_roman('MMVIII'))
print(RomanNumerals.from_roman('MDCLXVI'))