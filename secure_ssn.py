def mask_security_number(security_number):
    number_list = list(security_number)
    front_number = number_list[:-4]
    end_number = number_list[0:4] = "*", "*", "*", "*"
    full_number = list(front_number) + list(end_number)
    secured = ''.join(full_number)
    return secured


# test
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))
