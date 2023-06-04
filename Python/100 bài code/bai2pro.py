x = int(input("Nhập số tính giai thừa: "))

def fact(x):
    result = 1
    for i in range(1, x +1):
        result *= i
    return result

print(fact(x))