def check_bit4(input): 
    mask = 0b1000
    if input & mask > 0:
        return "on"
    else:
        return "off"
