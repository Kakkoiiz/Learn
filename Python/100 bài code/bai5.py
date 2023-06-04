# Định nghĩa một class có ít nhất 2 method:

# getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
# printString: in chuỗi vừa nhập sang chữ hoa.
# Thêm vào các hàm kiểm tra đơn giản để kiểm tra method của class.

class StrUpper:
    def __init__(self):
        self.a = ''
    def Nhap(self):
        self.a = input("Nhập: ")
    def printStr(self):
        print(self.a.upper())
text= StrUpper()
text.Nhap()
text.printStr()