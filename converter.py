from math import log2, ceil

def main():
    convert = int(input("Would you like to convert denary to binary(1) or binary to denary(2)  "))
    
    if convert == 1:
        d_to_b()
    elif convert == 2:
        b_to_d()
    else:
        print("Input a valid option")


def d_to_b():
    num = int(input("Please input your whole denary number: "))
    bits = num_of_bits(num)
    print(bits)

def b_to_d():
    print()

def num_of_bits(num):
    bits = ceil(log2(num))
    return bits

main()
