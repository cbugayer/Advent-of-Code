import re

ex1 = "BEGINING mul(2,5000000) mul(982,443)don't() STUFF mul(2,500000) mul(11982,4343463)do() \n STUFF mul(2,50000) don't() BEWTWEEN mul(2,5000) DONTS don't()mul(2,500)do() BEWTEEN mul(2,50) DOS do()  mul(2,5)  don't() ENDING DONT  mul(1,1)"
ex2 = "\nBEGINING mul(2,500000000) don't() STUFF mul(2,50000000) do() STUFF mul(2,5000000) don't() BEWTWEEN mul(2,500000) DONTS don't()mul(2,50000)do() BEWTEEN mul(2,5000) DOS do()  mul(2,500)  do() mul(2,50) do() DONT don't()  mul(2,5) do() ENDING DO  mul(1,1)"
ex3 = "BEGINING mul(2,50000000) do() mul(2,5000000) don't() \n STUFF mul(2,500000) do() STUFF mul(2,50000) don't() BEWTWEEN mul(2,5000) DONTS don't()mul(2,500)do() BEWTEEN mul(2,50) DOS do()  mul(2,5)  don't() ENDING DONT  mul(1,1)\n"

def get_ranges(text):
    input = text
    ranges = []
    to_add = 0

    while True:
        dont_ind = text.find("don't()")
        if dont_ind == -1: 
            break
        do_ind = text[dont_ind:].find("do()")
        if do_ind == -1:
            ranges.append([dont_ind + to_add, len(input)]) # could also be len(text) + dont_ind + to add
            break
        else:
            real_do_ind = do_ind + dont_ind 
            ranges.append([dont_ind + to_add, real_do_ind + to_add])
            text = text[real_do_ind + 4:]
            to_add += real_do_ind + 4

    return ranges

def not_in_range(start, end, range):
    if end <=  range[0]: return -1 
    elif start > range[1]: return 1
    else: return 0

def multiply(matc):
    to_mult = re.findall(r"\d{1,300}", matc)
    return int(to_mult[0]) * int(to_mult[1])    

def get_res(text):      
    result = 0
    regex = r"mul\(\d{1,300},\d{1,300}\)"
    matches = re.finditer(regex, text)
    ranges = get_ranges(text)

    for mach in matches:
        inside_Arang = False

        for rang in ranges:
            where_in_rang = not_in_range(mach.start(), mach.end(), rang)
            match where_in_rang:
                case -1:
                    break
                case 0: 
                    inside_Arang = True
                    break
                case 1:
                    continue
        if not inside_Arang: 
            result += multiply(mach.group(0))

    return result

with open("day 3/corrupted.txt", "r") as f:
    text = f.read()
print(get_res(text))


