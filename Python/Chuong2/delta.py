def Tinh_delta(a, b, c):
    delta = b**2 -4*a*c
    return delta

while True:
    try:
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))
        c = float(input("Nhập c: " ))
        break
    except ValueError:
        print("Nhập lại: ")
delta = Tinh_delta(a, b, c)
print("Delta cần tính là: ", delta)