# wap to find 2^n 
n = int(input("write a no. to 2^n :"))


# a = 1
# for b in range(n):
#     a = a * 2
# print(a)


def power_of_2(n):
    a = 1
    for b in range(n):
        a = a*2
    return a



print(power_of_2(n))

