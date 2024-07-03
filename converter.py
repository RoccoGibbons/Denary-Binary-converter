from math import log, ceil

def main():
    convert = input("Would you like to convert between denary and binary(1), denary and hex(2), or binary and hex(3) ")
    
    result = ""

    if convert == "1":
        convert2 = input("Would you like to convert denary to binary(1), or binary to denary(2)? ")

        if convert2 == "1":
            result = d_to_b()
        elif convert2 == "2":
            result = b_to_d()
        else:
            print("Input a valid option")
    
    elif convert == "2":
        convert2 = input("Would you like to convert denary to hex(1), or hex to denary(2) ")

        if convert2 == "1":
            result = "0x" + d_to_h()
        elif convert2 == "2":
            print()
            #hex to denary
        else:
            print("Input a valid option")

    elif convert == "3":
        convert2 = input("Would you like to convert binary to hex(1), or hex to binary(2) ")

        if convert2 == "1":
            #binary to hex
            print()
        elif convert2 == "2":
            #hex to binary
            print()
        else:
            print("Input a valid option")

    else:
        print("Input a valid option")
    
    print(result)


def num_input():
     while True:
        try:
            num = int(input("Please input your whole denary number: "))
        except ValueError:
            print("Input a valid number")
            continue
        else:
            break
     return num


def binary_input(): 
    invalid_nums = ['2', '3', '4', '5', '6', '7', '8', '9']
    while True:
        valid = True
        test = 0
        binary = input("Please input your binary number: ")
        try:
            int(binary)
        except ValueError:
            print("Input a valid binary number")
            continue
        else:
            for n in binary:
                if n in invalid_nums:
                    valid = False
            if valid == False:
                print("Input a valid binary number")
                continue
            break
    return binary



def d_to_b():
    num = num_input()
    bits = num_of_bits_bin(num)
    binary = ""
    
    for i in range(bits - 1, -1, -1):
        maxi = pow(2, i)
        if (num / maxi) >= 1:
            binary += "1"
            num = num - maxi
        else:
            binary += "0"

    return binary
        

def b_to_d():
    binary = binary_input()

    num = 0
    column = 1

    for i in range(len(binary) - 1, -1, -1):
        num += int(binary[i]) * column
        column *= 2

    return num


def d_to_h():
    num = num_input()
    bits = num_of_bits_hex(num)
    hexa = ""

    for i in range(bits - 1, -1, -1):
        maxi = pow(16, i)
        digit = num // maxi
        if digit < 10:
            hexa += str(digit)
        else:
            match digit:
                case 10:
                    hexa += "A"
                case 11:
                    hexa += "B"
                case 12:
                    hexa += "C"
                case 13:
                    hexa += "D"
                case 14:
                    hexa += "E"
                case 15:
                    hexa += "F"
                case _:
                    print("Something went wrong - hex match statement")
        num -= (maxi * digit)
    
    return hexa



def num_of_bits_bin(num):
    bits = ceil(log2(num, 2))
    return bits

def num_of_bits_hex(num):
    bits = ceil(log(num, 16))
    return bits


main()
