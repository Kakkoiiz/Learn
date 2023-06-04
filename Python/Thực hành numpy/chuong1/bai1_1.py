import numpy as np

# Tạo mảng 1D

one_dimesional_array = np.array([1, 2, 3, 4, 5])

# Tạo mảng 2D

two_dimesional_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

def printInfo(array):
    print("Kiểu dữ liệu của mảng: ", type(array))
    print("Kiểu dữ liệu của phần tử trong mảng: ", array.dtype)
    print("Kích thước của mảng: ", array.shape)
    print("Số chiều: ", array.ndim)
    print("Số phần tử: ", array.size)
    
printInfo(one_dimesional_array)
printInfo(two_dimesional_array)

# lấy giá trị trong mảng

print("phần tử đầu tiên của mảng 1D: ", one_dimesional_array[0])
print("Phần tử cuối cùng của mảng 1D: ",one_dimesional_array[-1])

print("Phần tử đầu tiên của mảng 2D: ", two_dimesional_array[0][0])
print("Phần tử cuối cùng của mảng 2D: ",two_dimesional_array[-1][-1])

# Lấy ra vị trí giá trị nhỏ nhất và lớn nhất của mảng

print("Vị trí giá trị lớn nhất của mảng 1D: ", np.argmax(one_dimesional_array))
print("Vị trí giá trị nhỏ nhất của mảng 1D: ", np.argmin(one_dimesional_array))


print("Vị trí giá trị lớn nhất của mảng 2D: ", np.argmax(two_dimesional_array))
print("Vị trí giá trị nhỏ nhất của mảng 2D: ", np.argmin(two_dimesional_array))

# Tính tổng các phần tử của mảng

print("Tổng các phần tử của mảng 1D: ", np.sum(one_dimesional_array))
print("Tổng các phần tử của mảng 2D: ", np.sum(two_dimesional_array))

# Tính trung bình cộng của các phần tử trong mảng

print("Trung bình cộng của các phần tử trong mảng 1D: ", np.mean(one_dimesional_array))
print("Trung bình cộng của các phần tử trong mảng 2D: ", np.mean(two_dimesional_array))