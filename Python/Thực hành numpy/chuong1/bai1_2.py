import numpy as np
from scipy import stats

# Tạo mảng 1D

one_dimesional_array = np.array([10, 10, 17, 29, 10, 23, 20, 17, 29, 17, 10, 20])

def printInfo(array):
    print("Tổng các phần tử trong mảng: ", np.sum(one_dimesional_array))
    print("Giá trị lớn nhất trong mảng: ", np.max(one_dimesional_array))
    print("Index của phần tử có giá trị lớn nhất: ", np.argmax(one_dimesional_array))
    print("Giá trị nhỏ nhất trong mảng: ", np.min(one_dimesional_array))
    print("Index của phần tử có giá trị nhỏ nhất: ", np.argmin(one_dimesional_array))
    
printInfo(one_dimesional_array)

# Thay đổi mảng

two_dimesional_array = np.reshape(one_dimesional_array, (3,4))

print("Mảng sau khi thay đổi kích thước:\n",two_dimesional_array)

# Tính tổng các phần từ của hàng và cột

print("Tổng các phần tử của mỗi hàng: ", np.sum(two_dimesional_array, axis=1))
print("Tổng các phần tử của mỗi cột: ", np.sum(two_dimesional_array, axis=0))

# Tính trung bình cộng của hàng và cột

print("Trung bình cộng các phần tử của mỗi hàng: ", np.mean(two_dimesional_array, axis=1))
print("Trung bình cộng các phần tửi của mỗi cột: ", np.mean(two_dimesional_array, axis=0))

# Tìm giá trị lớn nhất và nhỏ nhất của mỗi hàng 

print("Giá trị lớn nhất của mỗi hàng: ", np.max(two_dimesional_array, axis=1))
print("Giá trị nhỏ nhất của mỗi hàng: ", np.min(two_dimesional_array, axis=1))

# Tìm giá trị lớn nhất và nhỏ nhất của mỗi cột

print("Giá trị lớn nhất của mỗi cột: ", np.max(two_dimesional_array, axis=0))
print("Giá trị nhỏ nhất của mỗi cột: ", np.min(two_dimesional_array, axis=0))

# Tính trung vị của hàng và cột

print("Trung vị của mỗi hàng: ", np.median(two_dimesional_array, axis=1))
print("Trung vị của mỗi cột: ", np.median(two_dimesional_array, axis=0))

# Tính độ lệch chuẩn của mỗi hàng

print("Độ lệch chuẩn của mỗi hàng: ", np.std(two_dimesional_array,axis=0))
print("Độ lệch chuẩn của mỗi cột: ", np.std(two_dimesional_array,axis=0))

# Tìm phần tử xuất hiện nhiều nhất trong mảng
mode, count = stats.mode(one_dimesional_array,keepdims=True)
print("Phần tử xuất hiện nhiều nhất trong mảng: ", mode[0], "-số lần: " , count[0])
