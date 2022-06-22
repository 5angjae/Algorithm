# BOJ2608 로마 숫자

def rom_to_num(rom):
    total = 0
    i = 1
    while i < len(rom):
        if rom_dict[rom[i]] > rom_dict[rom[i-1]]:
            total += rom_dict[rom[i]] - rom_dict[rom[i-1]]
            i += 2
        else:
            total += rom_dict[rom[i-1]]
            i += 1

    if rom_dict[rom[len(rom) - 1]] <= rom_dict[rom[len(rom) - 2]]:
        total += rom_dict[rom[len(rom) - 1]]
    return total

def num_to_rom(num):
    one = num % 10 # 1의 자리
    ten = num % 100 // 10 # 10의 자리
    hun = num % 1000 // 100 # 100의 자리
    thou = num // 1000 # 1000의 자리
    rom = ""
    if thou == 0:
        pass
    elif 1 <= thou <= 3:
        rom += "M" * (thou)

    if hun == 0:
        pass
    elif 1 <= hun <= 3:
        rom += "C" * (hun)
    elif hun == 4:
        rom += "CD"
    elif 5 <= hun <= 8:
        rom += ("D" + ("C" * (hun - 5)))
    elif hun == 9:
        rom += "CM"

    if ten == 0:
        pass
    elif 1 <= ten <= 3:
        rom += "X" * (ten)
    elif ten == 4:
        rom += "XL"
    elif 5 <= ten <= 8:
        rom += ("L" + ("X" * (ten - 5)))
    elif ten == 9:
        rom += "XC"

    if one == 0:
        pass
    elif 1 <= one <= 3:
        rom += "I" * (one)
    elif one == 4:
        rom += "IV"
    elif 5 <= one <= 8:
        rom += ("V" + ("I" * (one - 5)))
    elif one == 9:
        rom += "IX"

    return rom

rom_dict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D":500, "M": 1000}

first_rom = input()
second_rom = input()

first_num = rom_to_num(first_rom)
second_num = rom_to_num(second_rom)


print(first_num + second_num)
print(num_to_rom(first_num + second_num))