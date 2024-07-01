from math import log2, ceil

def main():
    convert = input("Would you like to convert denary to binary(1) or binary to denary(2)  ")
    
    result = ""

    if convert == "1":
        result = d_to_b()
    elif convert == "2":
        result = b_to_d()
    else:
        print("Input a valid option")
    
    print(result)


def d_to_b():
    while True:
        try:
            num = int(input("Please input your whole denary number: "))
        except ValueError:
            print("Input a valid number")
            continue
        else:
            break

    bits = num_of_bits(num)
    
    binary = ""
    
    for i in range(bits - 1, -1, -1):
        max = pow(2, i)
        if (num / max) >= 1:
            binary += "1"
            num = num - max
        else:
            binary += "0"

    return binary
        

def b_to_d():
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

    num = 0
    column = 1

    for i in range(len(binary) - 1, -1, -1):
        num += int(binary[i]) * column
        column *= 2

    return num


def num_of_bits(num):
    bits = ceil(log2(num))
    return bits


main()
